import dataclasses
import typing
import xml.etree.ElementTree as ET

from pyupnp.utils import gsas


__all__ = [
    'StateVariable', 'Argument', 'Action', 'SCPD'
]


@dataclasses.dataclass
class StateVariable:
    send_events: bool
    multicast: bool

    name: str
    datatype: str
    ext_type: tuple[str, str] | None

    default: str | None
    allowed_values: list[str] | None
    allowed_range: tuple[int, int, int] | None

    @classmethod
    def parse_xml(cls, xml: ET.Element):
        send_events = xml.attrib.get('sendEvents', 'yes').lower() == 'yes'
        multicast = xml.attrib.get('multicast', 'no').lower() == 'yes'

        datatype = xml.find('{urn:schemas-upnp-org:service-1-0}dataType')
        ext_type = datatype.attrib.get('type')
        if ext_type is not None:
            ext_type = tuple(ext_type.rsplit(':', 1))
            if not ext_type[0].startswith('urn:'):
                ns = xml.find_namespace(ext_type[0])  # TODO
                ext_type = ns, ext_type[1]

        allowed_values = xml.find('{urn:schemas-upnp-org:service-1-0}allowedValueList')
        if allowed_values is not None:
            allowed_values = [i.text for i in allowed_values]

        allowed_range = xml.find('{urn:schemas-upnp-org:service-1-0}allowedValueRange')
        if allowed_range is not None:
            allowed_range = (
                gsas(xml, 'minimum', 0, int),
                gsas(xml, 'maximum', 0, int),
                gsas(xml, 'step', 1, int)
            )

        return cls(
            send_events, multicast,
            xml.find('{urn:schemas-upnp-org:service-1-0}name').text,
            datatype.text, ext_type,
            gsas(xml, 'defaultValue'),
            allowed_values, allowed_range
        )


@dataclasses.dataclass
class Argument:
    name: str
    direction: typing.Literal['IN', 'OUT']
    retval: bool
    type: StateVariable
    'A_ARG_TYPE_'

    @classmethod
    def parse_xml(cls, xml: ET.Element, state_variables):
        rsv = xml.find('{urn:schemas-upnp-org:service-1-0}relatedStateVariable').text
        return cls(
            xml.find('{urn:schemas-upnp-org:service-1-0}name').text,
            xml.find('{urn:schemas-upnp-org:service-1-0}direction').text.upper(),
            xml.find('{urn:schemas-upnp-org:service-1-0}retval') is not None,
            state_variables[rsv]
        )


@dataclasses.dataclass
class Action:
    name: str
    arguments: dict[str, Argument]

    @classmethod
    def parse_xml(cls, xml: ET.Element, state_variables):
        arguments = {}
        el = xml.find('{urn:schemas-upnp-org:service-1-0}argumentList')
        if el is not None:
            for i in el:
                arg = Argument.parse_xml(i, state_variables)
                arguments[arg.name] = arg

        return cls(
            xml.find('{urn:schemas-upnp-org:service-1-0}name').text,
            arguments
        )


@dataclasses.dataclass
class SCPD:
    actions: dict[str, Action]
    state_variables: dict[str, StateVariable]
    spec_version: tuple[int, int] = (1, 0)
    config_id: int = 1

    @classmethod
    def parse_xml(cls, xml: ET.Element):
        config_id = int(xml.attrib.get('configId', 1))

        spec_version = xml.find('{urn:schemas-upnp-org:service-1-0}specVersion')
        if spec_version is None:
            spec_version = (1, 0)
        else:
            spec_version = (gsas(spec_version, 'major', 1, int),
                            gsas(spec_version, 'minor', 0, int))

        state_variables = {}
        el = xml.find('{urn:schemas-upnp-org:service-1-0}serviceStateTable')
        if el is not None:
            for i in el:
                var = StateVariable.parse_xml(i)
                state_variables[var.name] = var

        actions = {}
        el = xml.find('{urn:schemas-upnp-org:service-1-0}actionList')
        if el is not None:
            for i in el:
                act = Action.parse_xml(i, state_variables)
                actions[act.name] = act

        return cls(actions, state_variables, spec_version, config_id)
