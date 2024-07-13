import xml.etree.ElementTree as ET

from pyupnp import Icon, GenericDeviceInfo
from pyupnp.client import Device, Service
from pyupnp.utils import gsa

__all__ = [
    'parse_device_description'
]


def parse_device_description(xml: ET.Element, location: str):
    base_url = gsa(xml, 'URLBase', location)
    config_id = int(xml.attrib.get('configId', 1))

    spec_version = xml.find('{urn:schemas-upnp-org:device-1-0}specVersion')
    if spec_version is None:
        spec_version = (1, 0)
    else:
        spec_version = (gsa(spec_version, 'major', 1, int),
                        gsa(spec_version, 'minor', 0, int))

    root_device = parse_device(xml.find('{urn:schemas-upnp-org:device-1-0}device'))

    for device in root_device.iter_all_devices():
        for icon in device.info.icons:
            icon._base_url = base_url

        for svc in device.services:
            svc._base_url = base_url

    return config_id, spec_version, root_device


def parse_device(xml: ET.Element):
    icons = []
    el = xml.find('{urn:schemas-upnp-org:device-1-0}iconList')
    if el is not None:
        for i in el:
            icon = Icon.parse_xml(i)
            if icon.url:
                icons.append(icon)

    info = GenericDeviceInfo(
        gsa(xml, 'UDN', ''),
        gsa(xml, 'friendlyName', ''),
        gsa(xml, 'manufacturer', ''),
        gsa(xml, 'manufacturerURL'),
        gsa(xml, 'modelDescription'),
        gsa(xml, 'modelName', ''),
        gsa(xml, 'modelNumber'),
        gsa(xml, 'modelURL'),
        gsa(xml, 'serialNumber'),
        gsa(xml, 'presentationURL'),
        gsa(xml, 'UPC'),
        xml.find('{urn:schemas-upnp-org:device-1-0}deviceType').text,
        icons
    )

    device = Device(info)

    el = xml.find('{urn:schemas-upnp-org:device-1-0}serviceList')
    if el is not None:
        for i in el:
            device.services.append(parse_service(i))

    el = xml.find('{urn:schemas-upnp-org:device-1-0}deviceList')
    if el is not None:
        for i in el:
            device.devices.append(parse_device(i))

    return device


def parse_service(xml: ET.Element):
    return Service(
        xml.find('{urn:schemas-upnp-org:device-1-0}serviceType').text,
        xml.find('{urn:schemas-upnp-org:device-1-0}serviceId').text,
        gsa(xml, 'SCPDURL', ''),
        gsa(xml, 'controlURL', ''),
        gsa(xml, 'eventSubURL', ''),
    )
