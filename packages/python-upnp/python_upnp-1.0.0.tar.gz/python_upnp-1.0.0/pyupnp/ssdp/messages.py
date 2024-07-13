import datetime
import typing

from multidict import CIMultiDictProxy, CIMultiDict

from pyupnp.utils import MCAST_GROUP, MCAST_PORT


__all__ = [
    'SSDPMessage',
    'NotifyMessage', 'NotifyAliveMessage', 'NotifyByeMessage', 'NotifyUpdateMessage',
    'SearchMessage', 'MulticastSearchMessage', 'UnicastSearchMessage',
    'ResponseMessage', 'TYPE_TO_START_LINE',
]

TYPE_TO_START_LINE = {
    None: b'HTTP/1.1 200 OK',
    'NOTIFY': b'NOTIFY * HTTP/1.1',
    'M-SEARCH': b'M-SEARCH * HTTP/1.1',
}


class SSDPMessage:
    method: str | None
    headers: CIMultiDictProxy
    remote_address: str = ""
    remote_port: int = 0
    local_address: str = ""
    local_port: int = 0

    def __init__(self, headers: CIMultiDict = None):
        if headers is None:
            headers = CIMultiDict()
        self.headers = CIMultiDictProxy(headers)

    def encode(self):
        res = [TYPE_TO_START_LINE[self.method]]
        for k, v in self._to_headers().items():
            res.append(f"{k}: {v}".encode())

        res.append(b'')
        res.append(b'')
        return b'\r\n'.join(res)

    def _to_headers(self) -> typing.MutableMapping:
        return CIMultiDict(self.headers)


class NotifyMessage(SSDPMessage):
    method = 'NOTIFY'

    subtype: str
    type: str
    usn: str
    boot_id: int
    config_id: int

    remote_address = MCAST_GROUP
    remote_port = MCAST_PORT

    def __init__(self, type: str, usn: str, boot_id: int, config_id: int, headers: CIMultiDict = None):
        super().__init__(headers)
        self.type = type
        self.usn = usn
        self.boot_id = boot_id
        self.config_id = config_id

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        res['HOST'] = '239.255.255.250:1900'
        res['NT'] = self.type
        res['NTS'] = self.subtype
        res['USN'] = self.usn
        res['BOOTID.UPNP.ORG'] = str(self.boot_id)
        res['CONFIGID.UPNP.ORG'] = str(self.config_id)
        return res

    def __repr__(self):
        return f'{type(self).__name__} NT={self.type} USN={self.usn}'


class NotifyAliveMessage(NotifyMessage):
    subtype = 'ssdp:alive'

    location: str
    server: str
    max_age: int
    search_port: int | None
    secure_location: str | None

    def __init__(self, type: str, usn: str, boot_id: int, config_id: int, location: str, server: str, max_age: int,
                 search_port: int | None = None, secure_location: str | None = None, headers: CIMultiDict = None):
        super().__init__(type, usn, boot_id, config_id, headers)
        self.location = location
        self.server = server
        self.max_age = max_age
        self.search_port = search_port
        self.secure_location = secure_location

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        res['LOCATION'] = self.location
        res['SERVER'] = self.server
        res['CACHE-CONTROL'] = "max-age=" + str(self.max_age)
        if self.search_port is not None:
            res['SEARCHPORT.UPNP.ORG'] = str(self.search_port)
        if self.secure_location is not None:
            res['SECURELOCATION.UPNP.ORG'] = self.secure_location
        return res


class NotifyByeMessage(NotifyMessage):
    subtype = 'ssdp:byebye'


class NotifyUpdateMessage(NotifyMessage):
    subtype = 'ssdp:update'

    location: str
    next_boot_id: int
    search_port: int | None
    secure_location: str | None

    def __init__(self, type: str, usn: str, boot_id: int, config_id: int, location: str, next_boot_id: int,
                 search_port: int | None = None, secure_location: str | None = None, headers: CIMultiDict = None):
        super().__init__(type, usn, boot_id, config_id, headers)
        self.location = location
        self.next_boot_id = next_boot_id
        self.search_port = search_port
        self.secure_location = secure_location

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        res['LOCATION'] = self.location
        res['NEXTBOOTID.UPNP.ORG'] = str(self.next_boot_id)
        if self.search_port is not None:
            res['SEARCHPORT.UPNP.ORG'] = str(self.search_port)
        if self.secure_location is not None:
            res['SECURELOCATION.UPNP.ORG'] = self.secure_location
        return res


class SearchMessage(SSDPMessage):
    method = 'M-SEARCH'

    is_multicast: bool
    host: str | None
    target: str
    user_agent: str | None

    def __init__(self, host: str | None, target: str, user_agent: str | None = None, headers: CIMultiDict = None):
        super().__init__(headers)
        self.host = host
        self.target = target
        self.user_agent = user_agent

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        if self.host is None:
            res['HOST'] = '239.255.255.250:1900'
        else:
            res['HOST'] = self.host
        res['MAN'] = '"ssdp:discover"'
        res['ST'] = self.target
        if self.user_agent is not None:
            res['USER-AGENT'] = self.user_agent
        return res

    def __repr__(self):
        return f'{type(self).__name__} ST={self.target} UA={self.user_agent}'


class MulticastSearchMessage(SearchMessage):
    is_multicast = True

    max_delay: int
    tcp_port: int | None
    friendly_name: str | None
    uuid: str | None

    remote_address = MCAST_GROUP
    remote_port = MCAST_PORT

    def __init__(self, target: str, user_agent: str | None, max_delay: int, tcp_port: int | None = None,
                 friendly_name: str | None = None, uuid: str | None = None, headers: CIMultiDict = None):
        super().__init__(None, target, user_agent, headers)
        self.max_delay = max_delay
        self.tcp_port = tcp_port
        self.friendly_name = friendly_name
        self.uuid = uuid

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        res['MX'] = str(self.max_delay)
        if self.tcp_port is not None:
            res['TCPPORT.UPNP.ORG'] = str(self.tcp_port)
        if self.friendly_name is not None:
            res['CPFN.UPNP.ORG'] = self.friendly_name
        if self.tcp_port is not None:
            res['CPUUID.UPNP.ORG'] = self.uuid
        res['Connection'] = 'close'
        return res


class UnicastSearchMessage(SearchMessage):
    is_multicast = False

    def __init__(self, host: str | tuple[str, int], target: str, user_agent: str | None = None,
                 headers: CIMultiDict = None):
        if isinstance(host, str):
            host = host.split(':', 1)

        if len(host) == 1:
            port = 1900
        else:
            port = int(host[1])
        host = host[0]

        super().__init__(f"{host}:{port}", target, user_agent, headers)
        self.remote_port = port
        self.remote_address = host


class ResponseMessage(SSDPMessage):
    method = None

    max_age: int
    date: datetime.datetime | None
    location: str
    server: str
    target: str
    usn: str
    boot_id: int
    config_id: int | None
    search_port: int | None
    secure_location: str | None

    def __init__(self, max_age: int, date: datetime.datetime | None, location: str, server: str, target: str, usn: str,
                 boot_id: int, config_id: int | None = None, search_port: int | None = None,
                 secure_location: str | None = None, headers: CIMultiDict = None):
        super().__init__(headers)
        self.max_age = max_age
        self.date = date
        self.location = location
        self.server = server
        self.target = target
        self.usn = usn
        self.boot_id = boot_id
        self.config_id = config_id
        self.search_port = search_port
        self.secure_location = secure_location

    def _to_headers(self) -> typing.MutableMapping:
        res = super()._to_headers()
        res['CACHE-CONTROL'] = "max-age=" + str(self.max_age)
        res['EXT'] = ''
        res['DATE'] = self.date.strftime('%a, %d %b %Y %H:%M:%S %Z')
        res['LOCATION'] = self.location
        res['SERVER'] = self.server
        res['ST'] = self.target
        res['USN'] = self.usn
        res['BOOTID.UPNP.ORG'] = str(self.boot_id)
        if self.config_id is not None:
            res['CONFIGID.UPNP.ORG'] = str(self.config_id)
        if self.search_port is not None:
            res['SEARCHPORT.UPNP.ORG'] = str(self.search_port)
        if self.secure_location is not None:
            res['SECURELOCATION.UPNP.ORG'] = self.secure_location
        return res

    def __repr__(self):
        return f'{type(self).__name__} ST={self.target} USN={self.usn}'
