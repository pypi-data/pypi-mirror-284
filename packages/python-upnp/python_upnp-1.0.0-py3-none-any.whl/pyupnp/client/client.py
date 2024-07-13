import asyncio
import time
import typing

from pyupnp.client import RootDevice, Device
from pyupnp.ssdp import (SSDPMessage, UnicastSearchMessage, MulticastSearchMessage, ResponseMessage, SearchMessage,
                         NotifyAliveMessage, NotifyByeMessage, create_ssdp_sender, SSDPSocket)
from pyupnp.utils import queue_get_with_timeout, detect_local_by_remote

__all__ = [
    'SSDPClient'
]


class SSDPClient(SSDPSocket):
    def __init__(self, local_addresses, *, user_agent: str = None, max_delay: int = 5,
                 friendly_name: str = None, loop=None):
        super().__init__(local_addresses, loop)
        self._user_agent = user_agent
        self._max_delay = max_delay
        self._friendly_name = friendly_name

        self._event_queue = asyncio.Queue()
        self._blocked_devices = set()
        self._devices = {}

    async def close(self):
        self._event_queue.put_nowait(('close', None))
        await super().close()

    async def _process_message(self, msg: SSDPMessage):
        if isinstance(msg, SearchMessage):
            return

        if isinstance(msg, ResponseMessage) or isinstance(msg, NotifyAliveMessage):
            udn = msg.usn.split('::')[0]
            if udn in self._blocked_devices:
                return

            dev = self._devices.get(udn)
            if dev is None:
                local_ipaddress = msg.local_address
                if local_ipaddress is None:
                    msg.local_address = detect_local_by_remote(msg.remote_address, self._local_addresses)

                self._devices[udn] = RootDevice(self, udn, msg.remote_address, local_ipaddress, msg.location, msg.max_age)

            else:
                if msg.local_address is not None and dev.local_address is None:
                    dev.local_address = msg.local_address
                dev._set_valid_until(msg.max_age)

        elif isinstance(msg, NotifyByeMessage):
            udn = msg.usn.split('::')[0]
            dev = self._devices.get(udn)
            if dev is not None:
                dev.close()

    def _remove_root_device(self, udn):
        if udn in self._devices:
            del self._devices[udn]
            self._event_queue.put_nowait(('remove', udn))

    # ==== Client ===

    def iter_devices(self) -> typing.Iterator[RootDevice]:
        for dev in self._devices.values():
            if not dev.closed:
                yield dev

    def get_device(self, udn: str) -> Device | None:
        dev = self._devices.get(udn)
        if dev is not None and not dev.closed:
            return dev

        for dev in self.iter_devices():
            if not dev.closed:
                for child in dev.iter_all_devices():
                    if child.info.udn == udn:
                        return child

        return None

    async def wait_for_event(self, *, timeout=None) -> tuple[str, str | None]:
        return await queue_get_with_timeout(self._event_queue, timeout, default=('timeout', None))

    async def wait_for_devices(self, *udns, timeout=None) -> Device | None:
        if not udns:
            raise ValueError('No devices specified')

        if timeout is None:
            return await self._wait_for_devices(udns)

        if timeout <= 0:
            for udn in udns:
                dev = self.get_device(udn)
                if dev is not None:
                    return dev
            return None

        try:
            return await asyncio.wait_for(self._wait_for_devices(udns), timeout)
        except asyncio.TimeoutError:
            return None

    async def _wait_for_devices(self, udns):
        while True:
            for udn in udns:
                dev = self.get_device(udn)
                if dev is not None:
                    return dev

            event, udn = await self.wait_for_event()
            if event is None:
                return None
            if event in {'add', 'update'} and udn in udns:
                return self.get_device(udn)

    # ==== Search ====

    async def search(self, address, target: str = "upnp:rootdevice", count=3, interval=0.2):
        msg = UnicastSearchMessage(f"{address[0]}:{address[1]}", target, self._user_agent)
        local_address = detect_local_by_remote(address[0], self._local_addresses)
        await self._search_on(local_address, 0, msg, count, interval)

    async def search_all(self, target: str = "upnp:rootdevice", count=3, interval=0.2):
        msg = MulticastSearchMessage(target, self._user_agent, self._max_delay, None, self._friendly_name)
        for address, interface in self._local_addresses:
            await self._search_on(address, interface, msg, count, interval)

    async def _search_on(self, local_address, interface, msg: SearchMessage, count, interval):
        with await create_ssdp_sender(local_address, interface, loop=self._loop) as proto:
            expire = time.monotonic() + self._max_delay

            for i in range(count):
                await proto.send(msg)
                await self._receive_on_search(interval, proto)

            remain = expire - time.monotonic()
            if remain > 0:
                await self._receive_on_search(expire - time.monotonic(), proto)

    async def _receive_on_search(self, timeout, proto):
        end = time.monotonic() + timeout
        while True:
            remain = end - time.monotonic()
            msg = await proto.get(timeout=remain)
            if msg is None:
                break

            await self._process_message(msg)
