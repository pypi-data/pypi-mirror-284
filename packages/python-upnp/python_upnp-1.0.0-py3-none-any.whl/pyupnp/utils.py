import asyncio
import functools
import io
import ipaddress
import sys
import xml.etree.ElementTree as ET

import aiohttp
import ifaddr

MCAST_GROUP = '239.255.255.250'
MCAST_PORT = 1900
MCAST_ADDRESS = (MCAST_GROUP, MCAST_PORT)

ET.register_namespace('s', 'http://schemas.xmlsoap.org/soap/envelope/')


def xml_to_bytes(root, decl=True, xmlns=None):
    xml = ET.ElementTree(root)
    with io.BytesIO() as f:
        xml.write(f, encoding='utf-8', xml_declaration=decl, default_namespace=xmlns)
        return f.getvalue()


async def http_get_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            res.raise_for_status()
            return await res.text()


def _gsa(ns, xml: ET.Element, attr, default=None, type: type = str):
    value = xml.find(f'{{{ns}}}{attr}')
    if value is None:
        return default
    try:
        return type(value.text)
    except (TypeError, ValueError):
        return default


gsa = functools.partial(_gsa, 'urn:schemas-upnp-org:device-1-0')
gsas = functools.partial(_gsa, 'urn:schemas-upnp-org:service-1-0')
gsac = functools.partial(_gsa, 'urn:schemas-upnp-org:control-1-0')


async def queue_get_with_timeout(queue, timeout, default=None, raise_exception=False):
    if timeout is not None and timeout <= 0:
        try:
            return queue.get_nowait()
        except asyncio.QueueEmpty:
            if raise_exception:
                raise TimeoutError() from None
            return default

    try:
        return await asyncio.wait_for(queue.get(), timeout)
    except asyncio.TimeoutError:
        if raise_exception:
            raise TimeoutError() from None
        return default


def get_ip_address(local_addresses: list[tuple[str, int]]) -> set[str]:
    res = set()
    adapters = ifaddr.get_adapters()
    for address, interface in local_addresses:
        if address and address != '0.0.0.0':
            res.add(address)
        else:
            for adapter in adapters:
                if adapter.index == interface:
                    for addr in adapter.ips:
                        if addr.is_IPv4:
                            res.add(addr.ip)
                break

    return res


def iface_name_to_index(iface_name: str) -> int | None:
    adapters = ifaddr.get_adapters()
    if iface_name.startswith('@'):
        iface_name = iface_name[1:]

        for adapter in adapters:
            for ip in adapter.ips:
                if ip.ip == iface_name:
                    return adapter.index
    else:
        for adapter in adapters:
            if adapter.name == iface_name or adapter.nice_name == iface_name or str(adapter.index) == iface_name:
                return adapter.index

    return None


def get_all_ifaces():
    for adapter in ifaddr.get_adapters():
        for ip in adapter.ips:
            if ip.is_IPv4 and ipaddress.IPv4Network(ip.ip).is_loopback:
                break
        else:
            yield '0.0.0.0', adapter.index


def parse_interfaces(args):
    local_addresses = []
    for address in args:
        address, pe, interface = address.partition('%')
        if not address:
            address = '0.0.0.0'
        if interface:
            index = iface_name_to_index(interface)
            if index is None:
                print(f"No interface found: {interface}", file=sys.stderr)
                sys.exit(1)
        else:
            index = 0
        local_addresses.append((address, index))

    return local_addresses


def detect_local_by_remote(remote_address: str, local_addresses: list[tuple[str, int]]) -> str | None:
    remote_address = ipaddress.IPv4Address(remote_address)
    adapters = ifaddr.get_adapters()

    for local_address, interface in local_addresses:
        for adapter in adapters:
            for addr in adapter.ips:
                if (addr.is_IPv4
                        and (interface == adapter.index or interface == 0)
                        and (addr.ip == local_address or not local_address or local_address == '0.0.0.0')):
                    network = ipaddress.IPv4Network(f'{addr.ip}/{addr.network_prefix}', strict=False)
                    if remote_address in network:
                        return addr.ip
