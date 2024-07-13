import asyncio
import logging

from pyupnp.ssdp import create_ssdp_receiver


__all__ = [
    'SSDPSocket',
]

_LOG = logging.getLogger('pyupnp.input')


class SSDPSocket:
    def __init__(self, local_addresses, loop=None):
        self._local_addresses = local_addresses
        self._loop = loop or asyncio.get_running_loop()
        self._protocol = None
        self._recv_task = None

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def open(self):
        self._protocol = await create_ssdp_receiver(self._local_addresses, loop=self._loop)
        self._recv_task = asyncio.create_task(self._process_messages(), name='SSDP Receiver')

    async def close(self):
        if self._protocol is not None:
            self._protocol.close()
            self._protocol = None
        if self._recv_task is not None:
            self._recv_task.cancel()
            self._recv_task = None

    @property
    def closed(self):
        return self._protocol is None

    async def _process_messages(self):
        while True:
            msg = await self._protocol.get()
            try:
                await self._process_message(msg)
            except Exception:
                _LOG.exception("Error processing message")

    async def _process_message(self, msg):
        raise NotImplementedError()
