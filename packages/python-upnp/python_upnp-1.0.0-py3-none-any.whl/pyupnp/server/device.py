from functools import cached_property
import xml.etree.ElementTree as ET

from pyupnp.device_info import GenericDeviceInfo
from pyupnp.utils import xml_to_bytes


class Device:
    def __init__(self, info: GenericDeviceInfo):
        self.info = info
        self._services = {}
        self._embedded_devices = {}

    def _dev_to_xml(self):
        info = self.info
        device = ET.Element('device')
        ET.SubElement(device, 'deviceType').text = info.device_type
        ET.SubElement(device, 'friendlyName').text = info.friendly_name
        ET.SubElement(device, 'manufacturer').text = info.manufacturer
        if info.manufacturer_url:
            ET.SubElement(device, 'manufacturerURL').text = info.manufacturer_url
        if info.model_description:
            ET.SubElement(device, 'modelDescription').text = info.model_description
        ET.SubElement(device, 'modelName').text = info.model_name
        if info.model_number:
            ET.SubElement(device, 'modelNumber').text = info.model_number
        if info.model_url:
            ET.SubElement(device, 'modelURL').text = info.model_url
        if info.serial_number:
            ET.SubElement(device, 'serialNumber').text = info.serial_number

        ET.SubElement(device, 'UDN').text = info.udn
        if info.upc:
            ET.SubElement(device, 'UPC').text = info.upc

        if info.icons:
            icons = ET.SubElement(device, 'iconList')
            for icon in info.icons:
                icons.append(icon.to_xml())

        if self._services:
            services = ET.SubElement(device, 'serviceList')
            for service in self._services.values():
                svc = ET.SubElement(services, 'service')
                ET.SubElement(svc, 'serviceType').text = service.type
                ET.SubElement(svc, 'serviceId').text = service.id
                ET.SubElement(svc, 'SCPDURL').text = f'/{self.info.udn}/{service.type}/scpd.xml'
                ET.SubElement(svc, 'controlURL').text = f'/{self.info.udn}/{service.type}/control'
                ET.SubElement(svc, 'eventSubURL').text = f'/{self.info.udn}/{service.type}/events'

        if self._embedded_devices:
            devices = ET.SubElement(device, 'deviceList')
            for device in self._embedded_devices.values():
                devices.append(device._dev_to_xml())

        if info.presentation_url:
            ET.SubElement(device, 'presentationURL').text = info.presentation_url

        return device

    @cached_property
    def descriptor(self):
        root = ET.Element('root')
        root.attrib['configId'] = str(1)

        version = ET.SubElement(root, 'specVersion')
        ET.SubElement(version, 'major').text = str(2)
        ET.SubElement(version, 'minor').text = str(0)

        root.append(self._dev_to_xml())

        root.attrib['xmlns'] = 'urn:schemas-upnp-org:device-1-0'
        return xml_to_bytes(root)

    def add_service(self, service):
        self._services[service.type] = service

    def get_service(self, st):
        return self._services.get(st)

    def iter_all_devices(self):
        yield self
        for embedded in self._embedded_devices.values():
            yield from embedded.iter_all_devices()

    def get_service_usns(self):
        res = {
            'upnp:rootdevice': {self.info.udn + '::upnp:rootdevice'},
        }

        for dev in self.iter_all_devices():
            res.setdefault(dev.info.device_type, set()).add(dev.info.udn + '::' + dev.info.device_type)
            res.setdefault(dev.info.udn, set()).add(dev.info.udn)

            for service in dev._services.values():
                for st in service.get_supported_types():
                    res.setdefault(st, set()).add(dev.info.udn + '::' + st)

        return res

    def get_device(self, uuid):
        for dev in self.iter_all_devices():
            if dev.info.udn == uuid:
                return dev
        return None
