#!/usr/bin/env python3
import sys, os
import signal
from getopt import getopt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

exec_file = os.path.basename(sys.argv[0])

help_text = f'''http-tunnel

Socket over HTTP.
Version: 0.5

Usage:
    {exec_file} -c [options]
    {exec_file} -s [options]

Options:
    -c, --client                    Run as client.
    -s, --server                    Run as server.

    -h, --host HOST                 Listen IP address. [Default: any]
    -p, --port PORT                 Listen port. [Default: 80 (or 443 if --cert is specified) on server, 22 on client]

    -r, --remote URL                URL of the remote server. [Default: http://127.0.0.1]
                                    (Only for client mode)
    -6, --ipv6                      Resolve remote FQDN with IPv6 before sending requests. [Default: IPv4]
                                    If resolve is failed, send requests with FQDN directly.
                                    (Only for client mode, added in version 0.4)
    --method METHOD                 HTTP method for sending data to the server. [Default: GET]
                                    Available options: GET, POST, PUT, DELETE, PATCH, WS(Added in version 0.5)
                                    (Only for client mode, added in version 0.3)
    -d, --destination HOST:PORT     Destination that server will connect to. [Default: 127.0.0.1:22]
                                    (Only for client mode)
    --no-ssl-verify                 Disable SSL certificate verification. [Default: SSL verification enabled]
                                    (Only for client mode, added in version 0.6)

    -m, --max-sessions NUM          Maximum tunnels that server will open at same time. [Default: 10]
                                    (Only for server mode)
    --cert FILE                     SSL certificate file for HTTPS, must be specified with --key.
                                    (Only for server mode, added in version 0.6)
    --key FILE                      SSL key file for HTTPS, must be specified with --cert.
                                    (Only for server mode, added in version 0.6)

    -b, --buffer BUFFER             Maximum size in bytes (per packet) that is sent to the tunnel. [Default: 32768]
                                    (Find the best number for yourself)
    -q, --queue QUEUE               Maximum packets that are sent to the tunnel at once. [Default: 10]
                                    (Find the best number for yourself)
    --reorder-buffer                Maximum packets can be held that were not received in order. [Default: 20]
                                    (Added in version 0.2)

    --help                          Show this message.
'''


def start_client(**kwargs):
    from http_tunnel.client import client

    host = kwargs.get('host', '')
    port = kwargs.get('port', 22)
    remote = kwargs.get('remote', None)
    if remote is not None:
        try:
            _r_host = remote.split('://')[1].split('/')[0].split(':')[0]
        except Exception:
            print('[E] Invalid remote URL.', end='\n\n')
            print(help_text)
            exit(1)
        if not _r_host or not remote.startswith('http'):
            print('[E] Invalid remote URL.', end='\n\n')
            print(help_text)
            exit(1)
    ipv6 = kwargs.get('ipv6', False)
    method = kwargs.get('method', None)
    if method not in (None, 'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'WS'):
        print('[E] Invalid arguments: method.', end='\n\n')
        print(help_text)
        exit(1)
    destination = kwargs.get('destination', None)
    noverify = kwargs.get('noverify', False)
    buffer = kwargs.get('buffer', None)
    queue = kwargs.get('queue', None)
    reorder = kwargs.get('reorder', None)

    client(host, port, remote, ipv6, method, destination, noverify, buffer, queue, reorder)


def start_server(**kwargs):
    from http_tunnel.server import server

    host = kwargs.get('host', '')
    max_sessions = kwargs.get('max', None)
    cert = kwargs.get('cert', None)
    key = kwargs.get('key', None)
    if type(cert) is not type(key):
        print('[E] Invalid arguments: cert and key must be specified together.', end='\n\n')
        print(help_text)
        exit(1)
    port = kwargs.get('port', 80 if cert is None else 443)
    buffer = kwargs.get('buffer', None)
    queue = kwargs.get('queue', None)
    reorder = kwargs.get('reorder', None)

    server(host, port, max_sessions, cert, key, buffer, queue, reorder)


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    try:
        signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    except Exception:
        pass

    try:
        (opts, args) = getopt(
            sys.argv[1:],
            'csh:p:r:6d:m:b:q:',
            [
                'help',
                'client',
                'server',
                'host=',
                'port=',
                'remote=',
                'ipv6',
                'method=',
                'destination=',
                'no-ssl-verify',
                'max-sessions=',
                'cert=',
                'key=',
                'buffer=',
                'queue=',
                'reorder-buffer='
            ]
        )
    except Exception as identifier:
        print('[E] Invalid arguments:', identifier, end='\n\n')
        print(help_text)
        exit(1)
    if len(opts) == 0:
        print('[E] Arguments required.', end='\n\n')
        print(help_text)
        exit(1)
    if len(args) > 0:
        print('[E] Invalid arguments:', args[0], end='\n\n')
        print(help_text)
        exit(1)

    _action = ''
    _args = {}

    try:
        for opt in opts:
            if opt[0] in ('-c', '--client'):
                if not _action:
                    _action = 'client'
            elif opt[0] in ('-s', '--server'):
                if not _action:
                    _action = 'server'
            elif opt[0] in ('-h', '--host'):
                _args['host'] = opt[1]
            elif opt[0] in ('-p', '--port'):
                _args['port'] = int(opt[1])
            elif opt[0] in ('-r', '--remote'):
                _args['remote'] = opt[1]
            elif opt[0] in ('-6', '--ipv6'):
                _args['ipv6'] = True
            elif opt[0] == '--method':
                _args['method'] = opt[1].upper()
            elif opt[0] in ('-d', '--destination'):
                _args['destination'] = opt[1]
            elif opt[0] == '--no-ssl-verify':
                _args['noverify'] = True
            elif opt[0] in ('-m', '--max-sessions'):
                _args['max'] = int(opt[1])
            elif opt[0] == '--cert':
                _args['cert'] = opt[1]
            elif opt[0] == '--key':
                _args['key'] = opt[1]
            elif opt[0] in ('-b', '--buffer'):
                _args['buffer'] = int(opt[1])
            elif opt[0] in ('-q', '--queue'):
                _args['queue'] = int(opt[1])
            elif opt[0] == '--reorder-buffer':
                _args['reorder'] = int(opt[1])
            elif opt[0] == '--help':
                print(help_text)
                exit(0)
    except Exception as identifier:
        print('[E] Invalid arguments:', identifier, end='\n\n')
        print(help_text)
        exit(1)

    if not _action:
        print('[E] Invalid arguments: running mode required.', end='\n\n')
        print(help_text)
        exit(1)

    if _action == 'client':
        start_client(**_args)
    elif _action == 'server':
        start_server(**_args)


if __name__ == '__main__':
    main()
