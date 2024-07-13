import asyncio
import logging

from multicast import MulticastSocket

from pyupnp.ssdp import SSDPMessage, parse_ssdp_message
from pyupnp.utils import queue_get_with_timeout, MCAST_ADDRESS, detect_local_by_remote

__all__ = [
    'SSDPProtocol', 'create_ssdp_protocol',
    'create_ssdp_sender', 'create_ssdp_receiver'
]

_LOG = logging.getLogger('pyupnp.messaging.in')


class SSDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, local_addresses):
        self._queue = asyncio.Queue()
        self.transport: asyncio.DatagramTransport | None = None
        self._local_addresses = local_addresses

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.transport is not None:
            self.transport.close()

    def connection_made(self, transport):
        self.transport = transport

    def connection_lost(self, exc):
        self.transport = None

    def datagram_received(self, data: bytes, remote_addr: tuple[str, int]) -> None:
        msg = parse_ssdp_message(data)

        msg.remote_address, msg.remote_port = remote_addr
        local_addr = self.transport.get_extra_info('sockname')
        msg.local_port = local_addr[1]
        msg.local_address = detect_local_by_remote(msg.remote_address, self._local_addresses)

        _LOG.debug(f'IN {msg.remote_address}:{msg.remote_port} -> {msg.local_address}:{msg.local_port}: {msg}')
        self._queue.put_nowait(msg)

    async def get(self, timeout=None) -> SSDPMessage | None:
        return await queue_get_with_timeout(self._queue, timeout)

    async def send(self, msg: SSDPMessage):
        _LOG.debug(f'OUT {msg.local_address}:{msg.local_port} -> {msg.remote_address}:{msg.remote_port}: {msg}')
        data = msg.encode()
        sock = self.transport.get_extra_info('socket')._sock
        if msg.local_address and msg.local_address != '0.0.0.0':
            sock.set_multicast_if(msg.local_address)
            self.transport.sendto(data, (msg.remote_address, msg.remote_port))
        else:
            for local_address in self._local_addresses:
                sock.set_multicast_if(*local_address)
                self.transport.sendto(data, (msg.remote_address, msg.remote_port))


async def create_ssdp_protocol(sock, local_addresses, *, loop=None):
    if loop is None:
        loop = asyncio.get_running_loop()

    _, protocol = await loop.create_datagram_endpoint(lambda: SSDPProtocol(local_addresses), sock=sock)
    return protocol


async def create_ssdp_receiver(local_addresses, *, loop=None) -> SSDPProtocol:
    sock = MulticastSocket()
    sock.setblocking(False)
    sock.reuse_addr = True

    sock.multicast_loop = False
    sock.multicast_ttl = 2

    sock.bind_multicast(MCAST_ADDRESS)
    for address, interface in local_addresses:
        sock.add_membership(MCAST_ADDRESS[0], address, interface)

    return await create_ssdp_protocol(sock, local_addresses, loop=loop)


async def create_ssdp_sender(local_addr="0.0.0.0", interface=0, *, loop=None) -> SSDPProtocol:
    sock = MulticastSocket()
    sock.setblocking(False)
    sock.reuse_addr = True

    sock.multicast_loop = False
    sock.multicast_ttl = 2

    sock.bind((local_addr, 0))
    sock.set_multicast_if(local_addr, interface)

    return await create_ssdp_protocol(sock, [(local_addr, interface)], loop=loop)
