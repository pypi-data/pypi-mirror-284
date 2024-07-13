import datetime

from aiohttp.http_parser import HeadersParser
from multidict import CIMultiDict

from pyupnp.ssdp.messages import (NotifyAliveMessage, NotifyUpdateMessage, NotifyByeMessage, MulticastSearchMessage,
                                  UnicastSearchMessage, ResponseMessage, TYPE_TO_START_LINE)


__all__ = [
    'parse_ssdp_message'
]

START_LINE_TO_TYPE = {v: k for k, v in TYPE_TO_START_LINE.items()}


def _get_max_age(value: str):
    for i in value.split(','):
        k, eq, v = i.strip().partition('=')
        if eq and k.strip() == 'max-age':
            return int(v.strip())

    return 0


def _pop_if_exists(headers, key, default=None):
    if key in headers:
        return headers.pop(key)
    return default


def parse_ssdp_message(datagram: bytes):
    datagram = datagram.splitlines()
    if not datagram:
        return None

    start_line = datagram[0]
    if start_line not in START_LINE_TO_TYPE:
        return None

    method = START_LINE_TO_TYPE[start_line]
    parser = HeadersParser()
    headers, raw = parser.parse_headers(datagram)
    headers = CIMultiDict(headers)

    if method == 'M-SEARCH':
        if headers.pop('MAN') != '"ssdp:discover"':
            return None

        host = headers.pop('HOST')
        target = headers.pop('ST')
        user_agent = _pop_if_exists(headers, 'USER-AGENT')

        if host == '239.255.255.250:1900' or host == '239.255.255.250':
            max_delay = int(headers.pop('MX'))
            tcp_port = _pop_if_exists(headers, 'TCPPORT.UPNP.ORG')
            friendly_name = _pop_if_exists(headers, 'CPFN.UPNP.ORG', '')
            uuid = _pop_if_exists(headers, 'CPUUID.UPNP.ORG')

            if tcp_port is not None:
                tcp_port = int(tcp_port)

            return MulticastSearchMessage(target, user_agent, max_delay, tcp_port, friendly_name, uuid, headers)
        else:
            return UnicastSearchMessage(host, target, user_agent, headers)

    if method == 'NOTIFY':
        host = headers.pop('HOST')

        if host not in ['239.255.255.250:1900', '239.255.255.250']:
            return None

        type = headers.pop('NT')
        subtype = headers.pop('NTS')
        usn = headers.pop('USN')

        boot_id = _pop_if_exists(headers, 'BOOTID.UPNP.ORG')
        config_id = _pop_if_exists(headers, 'CONFIGID.UPNP.ORG')

        if boot_id is not None:
            boot_id = int(boot_id)
        if config_id is not None:
            config_id = int(config_id)

        if subtype == NotifyByeMessage.subtype:
            return NotifyByeMessage(type, usn, boot_id, config_id, headers)

        location = headers.pop('LOCATION')
        search_port = _pop_if_exists(headers, 'SEARCHPORT.UPNP.ORG')
        secure_location = _pop_if_exists(headers, 'SECURELOCATION.UPNP.ORG')

        if search_port is not None:
            search_port = int(search_port)

        if subtype == NotifyAliveMessage.subtype:
            server = headers.pop('SERVER')
            max_age = _get_max_age(headers.pop('CACHE-CONTROL'))
            return NotifyAliveMessage(type, usn, boot_id, config_id, location, server, max_age, search_port,
                                      secure_location, headers)

        if subtype == NotifyUpdateMessage.subtype:
            next_boot_id = int(headers.pop('NEXTBOOTID.UPNP.ORG'))
            return NotifyUpdateMessage(type, usn, boot_id, config_id, location, next_boot_id, search_port,
                                       secure_location, headers)

        return None

    max_age = _get_max_age(headers.pop('CACHE-CONTROL'))

    date = _pop_if_exists(headers, 'DATE')
    if date is not None:
        date = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')

    headers.pop('EXT')
    location = headers.pop('LOCATION')
    server = headers.pop('SERVER')
    target = headers.pop('ST')
    usn = headers.pop('USN')
    boot_id = _pop_if_exists(headers, 'BOOTID.UPNP.ORG')
    config_id = _pop_if_exists(headers, 'CONFIGID.UPNP.ORG')
    search_port = _pop_if_exists(headers, 'SEARCHPORT.UPNP.ORG')
    secure_location = _pop_if_exists(headers, 'SECURELOCATION.UPNP.ORG')

    if boot_id is not None:
        boot_id = int(boot_id)

    if config_id is not None:
        config_id = int(config_id)

    return ResponseMessage(max_age, date, location, server, target, usn, boot_id, config_id, search_port,
                           secure_location, headers)
