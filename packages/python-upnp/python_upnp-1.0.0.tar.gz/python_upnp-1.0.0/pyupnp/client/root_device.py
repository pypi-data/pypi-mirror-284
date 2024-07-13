import asyncio
import logging
import time
import xml.etree.ElementTree as ET

from pyupnp import GenericDeviceInfo
from pyupnp.client import Device, parse_device_description
from pyupnp.utils import http_get_text


__all__ = [
    'RootDevice'
]

_LOG = logging.getLogger('pyupnp.client.root_device')


class RootDevice(Device):
    def __init__(self, client, udn, remote_address, local_address, location, max_age, ):
        super().__init__(GenericDeviceInfo(udn, '', '', ''), remote_address, local_address)

        self._client = client
        self.location = location
        self._max_age = max_age

        self._closed = False
        self._valid_until = None

        self._update_task = None
        self._set_valid_until(max_age)
        self._timeout_task = asyncio.create_task(self._device_timeout_waiter(), name=f'Device {udn} timeout waiter')

    async def _update_info(self):
        text = await http_get_text(self.location)
        root: ET.Element = ET.fromstring(text)
        config_id, version, root_device = parse_device_description(root, self.location)
        self.info = root_device.info
        self.services = root_device.services
        self.devices = root_device.devices

        for di in self.iter_all_devices():
            di.remote_address = self.remote_address
            di.local_address = self.local_address

            for svc in di.services:
                try:
                    await svc.load_scpd()
                except Exception as e:
                    _LOG.error(f"SCDP loading failed: {e}")

        self._client._event_queue.put_nowait(('update', self.info.udn))

    async def _device_timeout_waiter(self):
        while True:
            if self._valid_until is None:
                await asyncio.sleep(60)
                continue

            timeleft = self._valid_until - time.monotonic()
            if timeleft <= 0:
                self.close()
                break

            await asyncio.sleep(timeleft)

    def _set_valid_until(self, max_age):
        # The '_valid_until' attribute is the monotonic date when the root
        # device and its services and embedded devices become disabled.
        # '_valid_until' None means no aging is performed.
        if max_age:
            self._valid_until = time.monotonic() + max_age
        else:
            self._valid_until = None

        if self._update_task is not None and not self._update_task.done():
            self._update_task.cancel()

        self._update_task = asyncio.create_task(self._update_info(), name=f'Device {self.info.udn} info updater')

    @property
    def closed(self):
        return self._closed and self._update_task.done()

    def close(self):
        if not self._closed:
            self._closed = True
            if self._timeout_task is not None and asyncio.current_task() != self._timeout_task:
                self._timeout_task.cancel()

            self._client._remove_root_device(self.info.udn)
