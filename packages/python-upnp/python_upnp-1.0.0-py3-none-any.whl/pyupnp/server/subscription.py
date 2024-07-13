import asyncio
import logging
import time
import uuid
import xml.etree.ElementTree as ET

import aiohttp

from pyupnp.server import Service
from pyupnp.utils import xml_to_bytes

_LOG = logging.getLogger('pyupnp.subscription')


class Subscription:
    def __init__(self, service: Service, statevars: list[str] | None, callbacks: list[str], timeout: int):
        self.id = 'uuid:' + str(uuid.uuid4())
        self.service = service
        self.callbacks = callbacks
        self.timeout = time.monotonic() + timeout
        self._seq = 0

        ok = statevars is not None
        if ok:
            for var in statevars:
                try:
                    service.get_variable(var)
                except ValueError:
                    ok = False
        if not ok:
            statevars = None

        self.statevars = statevars

        self._task = asyncio.create_task(self._worker())
        self.service.subscribe(self)
        _LOG.info(f'SUBSCRIBED {self.id} TO {self.statevars} ({self.callbacks})')

    async def _worker(self):
        while self.timeout is not None:
            tw = self.timeout - time.monotonic()
            if tw <= 0:
                self.service.unsubscribe(self.id)
                _LOG.debug(f'TIMED OUT {self.id}')
                break

            try:
                await asyncio.sleep(tw)
            except asyncio.CancelledError:
                pass

    def reset_timeout(self, timeout: int | None):
        self.timeout = time.monotonic() + (timeout or 1800)
        self._task.cancel()
        _LOG.info(f'RENEWED {self.id} TO {timeout}')

    def cancel(self):
        self.service.unsubscribe(self.id)
        self.timeout = None
        self._task.cancel()
        _LOG.info(f'UNSUBSCRIBED {self.id}')

    def notify_changed(self, var_name, value):
        if self.statevars is None or any((i == var_name for i in self.statevars)):
            _LOG.info(f'CHANGED {self.id} : {var_name}={value!r}')
            asyncio.create_task(self._notify({
                var_name: value
            }))

    async def _notify(self, changed):
        headers = {
            'CONTENT-TYPE': 'text/xml; charset=utf-8',
            'NT': 'upnp:event',
            'NTS': 'upnp:propchange',
            'SID': self.id,
            'SEQ': str(self._seq),
        }

        root = ET.Element('e:propertyset')

        for name, value in changed.items():
            prop = ET.SubElement(root, 'e:property')
            ET.SubElement(prop, name).text = str(value)

        root.attrib['xmlns:e'] = 'urn:schemas-upnp-org:event-1-0'
        body = xml_to_bytes(root)

        async with aiohttp.ClientSession() as session:
            for callback in self.callbacks:
                try:
                    async with session.request('NOTIFY', callback, headers=headers, data=body) as resp:
                        resp.raise_for_status()
                except Exception:
                    _LOG.exception(f'NOTIFY {self.id} TO {callback} failed')
