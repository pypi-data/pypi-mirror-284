import asyncio
from argparse import ArgumentParser

from pyupnp.client import SSDPClient, Device
from pyupnp.utils import get_all_ifaces, parse_interfaces


def _state_variable_type_to_str(var):
    if var.ext_type is None:
        t = var.datatype
    else:
        t = f"{var.ext_type[0]}::{var.ext_type[1]}"

    if var.allowed_values is not None:
        t += ' {' + ', '.join(var.allowed_values) + '}'

    if var.allowed_range is not None:
        t += f" {{{var.allowed_range[0]}:{var.allowed_range[1]}:{var.allowed_range[2]}}}"

    if var.default is not None:
        t += f" = {var.default}"

    return t


def _dump_device_info(device):
    info = device.info
    print("=== Device Info ===")
    print(f"Type:          {info.device_type}")
    print(f"Name:          {info.friendly_name} ({info.presentation_url})")
    print(f"Manufacturer:  {info.manufacturer} ({info.manufacturer_url})")
    print(f"Model:         {info.model_name} [{info.model_number}] ({info.model_url})")
    print(f"               {info.model_description}")
    print(f"Serial Number: {info.serial_number}")
    print(f"UDN:           {info.udn}")
    print(f"UPC:           {info.upc}")

    if info.icons:
        print("Icons:")
        for icon in info.icons:
            print(f"{icon.width}x{icon.height}@{icon.depth} {icon.mimetype}: {icon.url}")

    for svc in device.services:
        print("    === Service Info ===")
        print(f"    ID: {svc.service_id}")
        print(f"    Type: {svc.service_type}")

        for i in svc.scpd.actions.values():
            args = ', '.join((f"{arg.direction} {arg.name}: {_state_variable_type_to_str(arg.type)}"
                              for arg in i.arguments.values()))
            print(f"    {i.name}({args})")

        for i in svc.scpd.state_variables.values():
            if i.name.startswith('A_ARG_TYPE_'):
                continue

            if i.multicast and i.send_events:
                attr = "MC+EV"
            elif i.multicast:
                attr = "MC"
            elif i.send_events:
                attr = "EV"
            else:
                attr = ""

            print(f"    {i.name}: {_state_variable_type_to_str(i)} {attr}")

    print()


async def _on_device(dev: Device, args):
    if not args.quiet:
        print(f'Found device {dev.info.udn} at {dev.remote_address}')

    if args.dump:
        for info in dev.iter_all_devices():
            _dump_device_info(info)

    if args.invoke:
        *udn, st, action = args.invoke.split('/')

        if udn:
            dev = dev.find_device(udn[0])

            if dev is None:
                print(f"No device found: {udn[0]}")
                return

        for svc in dev.services:
            if svc.service_type == st:
                break
        else:
            print(f"No service {st} in {dev.info.device_type}")
            return

        action = svc.scpd.actions.get(action)
        if action is None:
            print(f"No action {action} in {svc.service_type}")
            return

        i_args = {}
        for i in args.args:
            name, _, value = i.partition('=')
            i_args[name] = value

        res = await svc.invoke(action.name, i_args)

        print("Invoke result:")
        for name, value in res.items():
            print(f"{name}: {value}")
        print()


async def amain():
    parser = ArgumentParser()
    parser.add_argument('--user-agent', type=str, default='UPnP/1.0 DLNADOC/1.50 pyupnp/1.0.0',
                        help='Client user agent string.')
    parser.add_argument('--friendly-name', type=str, default='PyUPNP CLI',
                        help='Client friendly name.')
    parser.add_argument('--max-delay', type=int, choices=range(1, 6), default=5, metavar='[1-5]',
                        help='Maximum delay for multicast search in seconds.')
    parser.add_argument('-L', '--local-address', type=str, action='append', default=[],
                        metavar='ADDRESS[%IFACE]', help='Local address and interface. Can be specified multiple times.')

    parser.add_argument('-r', '--remote-address', type=str, default=None, metavar='ADDRESS[:PORT]',
                        help='Remote address and port for unicast SSDP discovery.')
    parser.add_argument('-t', '--target', type=str, default='upnp:rootdevice', help='Discovery target.')
    parser.add_argument('--count', type=int, default=3, help='Count of discovery requests to send.')
    parser.add_argument('--interval', type=float, default=0.2, help='Interval between discovery requests.')

    parser.add_argument('-u', '--udn', action='append', default=[],
                        help='Device UDN. Can be specified multiple times. If not specified, all devices will be '
                             'processed.')

    parser.add_argument('-d', '--dump', action='store_true', default=False,
                        help='Dump found devices information.')
    parser.add_argument('-i', '--invoke', type=str, metavar='[UDN/...]SERVICE_ID/ACTION',
                        help='Invoke action on specified service. Arguments are specified by --arg.')
    parser.add_argument('-a', '--args', type=str, nargs='+', default=[], metavar='ARG=VALUE',
                        help='Arguments to pass to action. Used with --invoke.')

    parser.add_argument('--quiet', action='store_true', help='Suppress console output.')

    args = parser.parse_args()

    if not args.local_address:
        local_addresses = list(get_all_ifaces())
    else:
        local_addresses = parse_interfaces(args.local_address)

    async with SSDPClient(local_addresses, user_agent=args.user_agent,
                          max_delay=args.max_delay, friendly_name=args.friendly_name) as client:
        if not args.quiet:
            print('Starting discovery...')

        target = args.target
        if args.udn and len(args.udn) == 1:
            target = args.udn[0]

        if args.remote_address:
            remote_address, _, port = args.remote_address.partition(':')
            if port:
                port = int(port)
            else:
                port = 1900
            task = client.search((remote_address, port), target, args.count, args.interval)
        else:
            task = client.search_all(target, args.count, args.interval)

        if args.udn:
            task = asyncio.create_task(task)
            udns = set(args.udn)
            while udns:
                if not args.quiet:
                    print(f'Waiting for {len(udns)} devices...')

                dev = await client.wait_for_devices(*udns)
                udns.remove(dev.info.udn)
                await _on_device(dev, args)

            _ = task
        else:
            await task

            if not args.quiet:
                print('Discovery complete.')

            for dev in client.iter_devices():
                await _on_device(dev, args)


def main():
    asyncio.run(amain())


if __name__ == '__main__':
    main()
