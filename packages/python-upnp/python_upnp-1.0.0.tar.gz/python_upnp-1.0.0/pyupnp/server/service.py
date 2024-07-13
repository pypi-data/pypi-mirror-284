import inspect
import types

from pyupnp import soap


__all__ = [
    'action',
    'StateVariable',
    'Service'
]


def action(name):
    def _wrapper(func):
        func._scpd_action = name
        return func

    return _wrapper


def _parse_actions(cls):
    callbacks = {}
    for i in dir(cls):
        if i.startswith('_'):
            continue

        value = getattr(cls, i)
        if not inspect.isfunction(value):
            continue

        action_info = getattr(value, '_scpd_action', None)
        if action_info is None:
            continue

        callbacks[action_info] = value

    return callbacks


class StateVariable:
    def __init__(self, name: str, default=None, *, immutable=False):
        self.name = name
        self.default = default
        self.immutable = immutable

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.get_value(instance)

    def __set__(self, instance, value):
        if self.immutable:
            raise AttributeError(f'{self.name} is immutable')

        setattr(instance, '_statevar_' + self.name, value)
        instance.notify_changed(self.name, value)

    def __delete__(self, instance):
        if self.immutable:
            raise AttributeError(f'{self.name} is immutable')

        setattr(instance, '_statevar_' + self.name, self.default)
        instance.notify_changed(self.name, self.default)

    def get_value(self, instance):
        return getattr(instance, '_statevar_' + self.name, self.default)


class ServiceMeta(type):
    _actions: types.MappingProxyType
    _variables: types.MappingProxyType

    def __new__(mcs, name, bases, ns):
        if name == 'Service' and not bases:
            return type.__new__(mcs, name, bases, ns)

        if len(bases) != 1 or bases[0] != Service:
            raise ValueError(f'{name} must extend directly')

        state_vars = {}
        actions = {}
        for name, value in ns.items():
            if name.startswith('_'):
                continue

            if isinstance(value, StateVariable):
                state_vars[value.name] = value

            elif inspect.isfunction(value):
                action_info = getattr(value, '_scpd_action', None)
                if action_info is not None:
                    actions[action_info] = value

        ns['_actions'] = types.MappingProxyType(actions)
        ns['_variables'] = types.MappingProxyType(state_vars)
        return type.__new__(mcs, name, bases, ns)


class Service(metaclass=ServiceMeta):
    type: str
    id: str
    scpd: bytes

    def __init__(self):
        self._subscriptions = {}

    def invoke(self, action: str, args: dict[str, str]) -> dict[str, str]:
        cb = type(self)._actions.get(action)
        if cb is None:
            raise soap.SOAPError(401, 'Action not found')

        return cb(self, args)

    def get_variable(self, name: str):
        variable = type(self)._variables.get(name)
        if variable is None:
            raise ValueError()

        return variable.get_value(self)

    def get_supported_types(self):
        base, ver = self.type.rsplit(':', 1)
        for i in range(int(ver) + 1):
            yield base + ':' + str(i)

    def notify_changed(self, var_name, value):
        for sub in self._subscriptions.values():
            sub.notify_changed(var_name, value)

    def get_subscription(self, sid):
        return self._subscriptions.get(sid)

    def subscribe(self, sub):
        self._subscriptions[sub.id] = sub

    def unsubscribe(self, sid):
        del self._subscriptions[sid]
