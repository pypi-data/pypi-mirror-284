import xml.etree.ElementTree as ET

import aiohttp

from pyupnp.utils import xml_to_bytes, gsac


def _build(suffix, service_type, action, args):
    root = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
    root.attrib['s:encodingStyle'] = 'http://schemas.xmlsoap.org/soap/encoding/'
    body = ET.SubElement(root, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    act = ET.SubElement(body, f'u:{action}{suffix}')
    act.attrib['xmlns:u'] = service_type

    for k, v in args.items():
        ET.SubElement(act, k).text = str(v)

    return xml_to_bytes(root)


def build_request(service_type, action, args):
    return _build('', service_type, action, args)


def build_response(service_type, action, res):
    return _build('Response', service_type, action, res)


def parse_request(text):
    root = ET.fromstring(text)
    body: ET.Element = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')

    called = []
    for method in body:
        args = {}
        for arg in method:
            args[arg.tag] = arg.text or ''
        st, _, name = method.tag[1:].partition('}')
        called.append((st, name, args))

    return called


def parse_response(text, service_type, action):
    action += 'Response'

    for st, act, resp in parse_request(text):
        if st == service_type and act == action:
            return resp
    return None


def parse_fault(text):
    root = ET.fromstring(text)
    error = root.find(
        '{http://schemas.xmlsoap.org/soap/envelope/}Body'
        '/{http://schemas.xmlsoap.org/soap/envelope/}Fault'
        '/{http://schemas.xmlsoap.org/soap/envelope/}detail'
        '/{urn:schemas-upnp-org:control-1-0}UPnPError'
    )
    code = gsac(error, 'errorCode', 0, int)
    desc = gsac(error, 'errorDescription')
    return code, desc


def build_fault(code, desc=None):
    root = ET.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
    root.attrib['encodingStyle'] = 'http://schemas.xmlsoap.org/soap/encoding/'
    fault = ET.SubElement(root, '{http://schemas.xmlsoap.org/soap/envelope/}Fault')
    ET.SubElement(fault, 'faultCode').text = 's:Client'
    ET.SubElement(fault, 'faultstring').text = 'UPnPError'
    detail = ET.SubElement(fault, 'detail')
    error = ET.SubElement(detail, 'UPnPError')
    error.attrib['xmlns'] = 'urn:schemas-upnp-org:control-1-0'
    ET.SubElement(error, 'errorCode').text = str(code)
    if desc:
        ET.SubElement(error, 'errorDescription').text = desc

    return xml_to_bytes(root)


class SOAPError(Exception):
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc


async def invoke_request(control_url, service_type, action, args):
    data = build_request(service_type, action, args)
    headers = {
        'Content-type': 'text/xml; charset="utf-8"',
        'Soapaction': f'{service_type}#{action}',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(control_url, data=data, headers=headers) as res:
            text = await res.text()
            is_fault = res.status != 200

    if is_fault:
        code, desc = parse_fault(text)
        raise SOAPError(code, desc)

    return parse_response(text, service_type, action)
