import dataclasses
import urllib.parse
import xml.etree.ElementTree as ET
from functools import cached_property

from pyupnp import soap, GenericDeviceInfo
from pyupnp.client.scpd import SCPD
from pyupnp.utils import http_get_text

__all__ = [
    'Service',
    'Device',
]


@dataclasses.dataclass
class Service:
    service_type: str
    service_id: str
    scpd_url: str
    control_url: str
    event_sub_url: str

    scpd: SCPD = None
    _base_url: str = None

    @cached_property
    def full_scpd_url(self):
        return urllib.parse.urljoin(self._base_url, self.scpd_url)

    @cached_property
    def full_control_url(self):
        return urllib.parse.urljoin(self._base_url, self.control_url)

    @cached_property
    def full_event_sub_url(self):
        return urllib.parse.urljoin(self._base_url, self.event_sub_url)

    async def load_scpd(self):
        text = await http_get_text(self.full_scpd_url)
        root: ET.Element = ET.fromstring(text)

        self.scpd = SCPD.parse_xml(root)

    async def invoke(self, action, args):
        action = self.scpd.actions[action]
        arguments = action.arguments
        if set(args) != set((name for name in arguments if arguments[name].direction == 'IN')):
            raise ValueError("argument mismatch")

        return await soap.invoke_request(self.full_control_url, self.service_type, action.name, args)


class Device:
    def __init__(self, info: GenericDeviceInfo, remote_address=None, local_address=None):
        self.info = info
        self.remote_address = remote_address
        self.local_address = local_address
        self.services = []
        self.devices = []

    def iter_all_devices(self):
        yield self
        for dev in self.devices:
            yield from dev.iter_all_devices()

    def find_device(self, udn):
        for dev in self.iter_all_devices():
            if dev.udn == udn:
                return dev
        return None
