# PyUPnP

UPnP library in pure python. Client and server. Typed.

## Installation

```shell
pip install python-upnp
```

## Usage

### CLI Client

```
$ pyupnp_client --help
usage: pyupnp_client [-h] [--user-agent USER_AGENT] [--friendly-name FRIENDLY_NAME] [--max-delay [1-5]]
                     [-L ADDRESS[%IFACE]] [-r ADDRESS[:PORT]] [-t TARGET] [--count COUNT]
                     [--interval INTERVAL] [-u UDN] [-d] [-i [UDN/...]SERVICE_ID/ACTION]
                     [-a ARG=VALUE [ARG=VALUE ...]] [--quiet]

options:
  -h, --help            show this help message and exit
  --user-agent USER_AGENT
                        Client user agent string.
  --friendly-name FRIENDLY_NAME
                        Client friendly name.
  --max-delay [1-5]     Maximum delay for multicast search in seconds.
  -L ADDRESS[%IFACE], --local-address ADDRESS[%IFACE]
                        Local address and interface. Can be specified multiple times.
  -r ADDRESS[:PORT], --remote-address ADDRESS[:PORT]
                        Remote address and port for unicast SSDP discovery.
  -t TARGET, --target TARGET
                        Discovery target.
  --count COUNT         Count of discovery requests to send.
  --interval INTERVAL   Interval between discovery requests.
  -u UDN, --udn UDN     Device UDN. Can be specified multiple times. If not specified, all devices will be processed.
  -d, --dump            Dump found devices information.
  -i [UDN/...]SERVICE_ID/ACTION, --invoke [UDN/...]SERVICE_ID/ACTION
                        Invoke action on specified service. Arguments are specified by --arg.
  -a ARG=VALUE [ARG=VALUE ...], --args ARG=VALUE [ARG=VALUE ...]
                        Arguments to pass to action. Used with --invoke.
  --quiet               Suppress console output.

```



## License

MIT License. Full test available in LICENSE file.
