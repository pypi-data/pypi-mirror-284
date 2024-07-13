import logging
import re
import typing

from aiohttp import web

from pyupnp import soap
from pyupnp.server import Subscription


_LOG = logging.getLogger('pyupnp.invoke')


class WebServer(web.Application):
    def __init__(self, ips: typing.Iterable[str], port: int):
        super().__init__()
        self.__ips = tuple(ips)
        self.__port = port
        self.__runner = web.AppRunner(self)
        self.__sites = []

    async def open(self):
        await self.__runner.setup()

        for address in self.__ips:
            self.__sites.append(web.TCPSite(self.__runner, address, self.__port))

        for site in self.__sites:
            await site.start()

    async def close(self):
        if self.__sites:
            await self.__runner.cleanup()
            self.__sites.clear()


class ServerWebMixin:
    __slots__ = ('__device', )

    def __init__(self, device):
        self.__device = device

    def get_routes(self):
        return [
            web.get('/{uuid}/desc.xml', self.__handler_get_desc),
            web.get('/{uuid}/{st}/scpd.xml', self.__handler_get_scpd),
            web.post('/{uuid}/{st}/control', self.__handler_post_control),
            web.route('SUBSCRIBE', '/{uuid}/{st}/events', self.__handler_subscribe_events),
            web.route('UNSUBSCRIBE', '/{uuid}/{st}/events', self.__handler_unsubscribe_events),
        ]

    def __get_device(self, request):
        uuid = request.match_info['uuid']
        device = self.__device.get_device(uuid)
        if device is None:
            raise web.HTTPNotFound()

        return device

    def __get_service(self, request):
        device = self.__get_device(request)
        st = request.match_info['st']
        service = device.get_service(st)
        if service is None:
            raise web.HTTPNotFound()

        return service

    def __get_subscription(self, request):
        sid = request.headers.get('SID')
        if sid is None:
            raise web.HTTPPreconditionFailed()

        service = self.__get_service(request)

        sub = service.get_subscription(sid)
        if sub is None:
            raise web.HTTPPreconditionFailed()

        return sub

    async def __handler_get_desc(self, request):
        device = self.__get_device(request)
        return web.Response(content_type='text/xml', charset='utf-8', body=device.descriptor)

    async def __handler_get_scpd(self, request):
        service = self.__get_service(request)
        return web.Response(content_type='text/xml', charset='UTF-8', body=service.scpd)

    async def __handler_post_control(self, request: web.Request):
        service = self.__get_service(request)

        text = await request.text()
        req = soap.parse_request(text)
        if len(req) != 1:
            raise web.HTTPInternalServerError()

        service_type, action, args = req[0]

        try:
            res = self.__invoke(service, service_type, action, args)
        except soap.SOAPError as e:
            _LOG.exception(f'INVOKE FAILED {service.id}/{action}({args}) -> {e.code} {e.desc}')
            res = soap.build_fault(e.code, e.desc)
            status = 500
        else:
            _LOG.info(f'INVOKE {service.id}/{action}({args}) -> {res}')
            res = soap.build_response(service_type, action, res)
            status = 200

        return web.Response(status=status, content_type='text/xml', charset='UTF-8', body=res)

    async def __handler_subscribe_events(self, request: web.Request):
        timeout = request.headers.get('TIMEOUT')
        if timeout is not None:
            timeout = timeout.lower().replace('second-', '')
            if timeout == 'infinite':
                timeout = -1
            else:
                timeout = int(timeout)

        if request.headers.get('NT') == 'upnp:event':
            callback = request.headers.get('CALLBACK')
            if callback is None:
                raise web.HTTPPreconditionFailed()
            callback = callback.removeprefix('<').removesuffix('>')
            callback = re.split(r'>\s*,?\s*<', callback)

            statevar = request.headers.get('STATEVAR')
            if statevar is not None:
                statevar = statevar.split(',')

            service = self.__get_service(request)
            sub = Subscription(service, statevar, callback, timeout)
        else:
            sub = self.__get_subscription(request)
            sub.reset_timeout(timeout)

        headers = {
            'SID': sub.id,
            'TIMEOUT': f'Second-{sub.timeout}'
        }
        if sub.statevars is not None:
            headers['ACCEPTED-STATEVAR'] = ','.join(sub.statevars)

        return web.Response(headers=headers)

    async def __handler_unsubscribe_events(self, request: web.Request):
        sub = self.__get_subscription(request)
        sub.cancel()
        return web.Response()

    @staticmethod
    def __invoke(service, service_type, action, args):
        if service_type == 'urn:schemas-upnp-org:control-1-0' and action == 'QueryStateVariable':
            var_name = args.get('varName')
            if var_name is None:
                raise web.HTTPBadRequest()

            try:
                return service.get_variable(var_name)
            except Exception:
                raise soap.SOAPError(404, 'Variable not found')

        if service_type.rsplit(':', 1)[0] != service.type.rsplit(':', 1)[0]:
            raise web.HTTPBadRequest()

        try:
            return service.invoke(action, args)
        except NotImplementedError:
            raise soap.SOAPError(602, 'Not implemented')
        except ValueError:
            raise soap.SOAPError(600, 'Invalid arguments')
        except Exception as e:
            raise soap.SOAPError(501, str(e))
