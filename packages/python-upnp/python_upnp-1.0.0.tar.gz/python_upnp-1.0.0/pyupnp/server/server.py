import asyncio
import datetime

from pyupnp.server import Device
from pyupnp.server.web import WebServer, ServerWebMixin
from pyupnp.ssdp import SSDPMessage, SearchMessage, MulticastSearchMessage, ResponseMessage, \
    NotifyAliveMessage, NotifyByeMessage, SSDPSocket
from pyupnp.utils import get_ip_address, detect_local_by_remote


class SSDPServer(SSDPSocket):
    def __init__(self, device: Device, local_addresses, *, server_name: str = None,
                 notify_interval: int = 900, http_port: int = 8080, loop=None):
        super().__init__(local_addresses, loop)
        self._allowed_ips = get_ip_address(self._local_addresses)
        self._device = device
        self._server_name = server_name
        self._notify_interval = notify_interval
        self._http_port = http_port

        self._nt2usn: dict[str, str] = device.get_service_usns()
        self._notify_task = None
        self._stopper = self._loop.create_future()

        self._web = WebServer(self._allowed_ips, http_port)
        self._web.add_routes(ServerWebMixin(device).get_routes())

    async def _process_message(self, msg: SSDPMessage):
        if not isinstance(msg, SearchMessage):
            return

        if msg.target == 'ssdp:all':
            for nt, usns in self._nt2usn.items():
                await self._send_response(msg, nt)
            return

        if msg.target not in self._nt2usn:
            return

        if isinstance(msg, MulticastSearchMessage):
            await asyncio.sleep(0.3)

        await self._send_response(msg, msg.target)

    async def _notify_task_main(self):
        while True:
            try:
                await self._send_alive()
            except Exception:
                pass

            await asyncio.sleep(self._notify_interval)

    # === Management ===

    async def open(self):
        await super().open()
        await self._web.open()
        self._notify_task = self._loop.create_task(self._notify_task_main(), name='Server Notify Task')

    async def close(self):
        if self._notify_task:
            self._notify_task.cancel()
        if self._protocol:
            await self._send_goodbye()
        await self._web.close()
        await super().close()

    async def run(self):
        async with self:
            try:
                await self._stopper
            except asyncio.CancelledError:
                pass

    def stop(self):
        self._stopper.set_result(None)

    # === Send ===

    async def _send_response(self, msg: SearchMessage, st):
        local_address = msg.local_address
        if not local_address or local_address == '0.0.0.0':
            local_address = detect_local_by_remote(msg.remote_address, self._local_addresses)

        for usn in self._nt2usn[st]:
            res = ResponseMessage(
                max_age=self._notify_interval * 2 + 10,
                date=datetime.datetime.now(tz=datetime.timezone.utc),
                target=st,
                usn=usn,
                server=self._server_name,
                location=f'http://{local_address}:{self._http_port}/{self._device.info.udn}/desc.xml',
                boot_id=1
            )
            res.remote_address = msg.remote_address
            res.remote_port = msg.remote_port
            await self._protocol.send(res)

    async def _send_goodbye(self):
        for st, usns in self._nt2usn.items():
            for usn in usns:
                msg = NotifyByeMessage(
                    type=st, usn=usn, boot_id=1, config_id=1
                )
                await self._protocol.send(msg)

    async def _send_alive(self):
        for address in self._allowed_ips:
            for i in range(2):
                for st, usns in self._nt2usn.items():
                    for usn in usns:
                        msg = NotifyAliveMessage(
                            type=st,
                            usn=usn,
                            boot_id=1,
                            config_id=1,
                            location=f'http://{address}:{self._http_port}/{self._device.info.udn}/desc.xml',
                            server=self._server_name,
                            max_age=self._notify_interval * 2 + 10
                        )
                        await self._protocol.send(msg)
