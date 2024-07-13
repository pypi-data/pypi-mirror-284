import dataclasses
import urllib.parse
import xml.etree.ElementTree as ET
from functools import cached_property

from pyupnp.utils import gsa


__all__ = [
    'Icon', 'GenericDeviceInfo'
]


@dataclasses.dataclass
class Icon:
    mimetype: str
    width: int
    height: int
    depth: int
    url: str
    _base_url: str = None

    @cached_property
    def full_url(self):
        return urllib.parse.urljoin(self._base_url, self.url)

    def to_xml(self):
        icon = ET.Element('icon')
        ET.SubElement(icon, 'mimetype').text = self.mimetype
        ET.SubElement(icon, 'width').text = int(self.width)
        ET.SubElement(icon, 'height').text = int(self.height)
        ET.SubElement(icon, 'depth').text = int(self.depth)
        ET.SubElement(icon, 'url').text = self.url
        return icon

    @classmethod
    def parse_xml(cls, xml: ET.Element):
        return cls(
            gsa(xml, 'mimetype', ''),
            gsa(xml, 'width', 0, int),
            gsa(xml, 'height', 0, int),
            gsa(xml, 'depth', 0, int),
            gsa(xml, 'url')
        )


@dataclasses.dataclass
class GenericDeviceInfo:
    udn: str

    friendly_name: str
    manufacturer: str
    model_name: str

    manufacturer_url: str | None = None
    model_description: str | None = None
    model_number: str | None = None
    model_url: str | None = None
    serial_number: str | None = None
    presentation_url: str | None = None
    upc: str | None = None

    device_type: str = ''

    icons: list[Icon] = dataclasses.field(default_factory=list)
