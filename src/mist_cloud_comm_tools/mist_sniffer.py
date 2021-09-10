#!/usr/bin/env python3
"""
Mist cloud AMQP message sniffer.
"""

__copyright__ = 'Thinnect Inc. 2021'
__license__ = 'MIT'


import pika
import argparse
import socket
import ssl
import os

from google.protobuf.message import DecodeError

from .mist_pb2 import MistMessage

from .formatters import format_proto_timestamp
from .parsers import arg_hex2int

verbose = False


def message_received(ch, method, properties, body):
    if verbose:
        print(f'RCV {method.routing_key}: {body.hex().upper()}')

    mm = MistMessage()
    try:
        mm.ParseFromString(body)
    except DecodeError:
        print(f'\nERROR PARSING:\n{method.routing_key}\n{body.hex()}\n')
        return

    print(f'@{format_proto_timestamp(mm.timestamp)}'
          f' {{{mm.group:04X}}}{mm.source:016X}->{mm.destination:016X}[{mm.amid:04X}]'
          f' {len(mm.payload):3d}: {mm.payload.hex().upper()}'
          f' {mm.lqi:02X}:{mm.rssi:3d} ({mm.channel:2d})')


def main():

    parser = argparse.ArgumentParser(description='Sniff mist messages from a RabbitMQ exchange.')
    parser.add_argument('--server', default=os.environ.get('MIST_RABBITMQ_SERVER', 'server.rabbit.mq'),
                        help='The server to use for sniffing.')
    parser.add_argument('--username', default=os.environ.get('MIST_RABBITMQ_USERNAME', 'bugsbunny'))
    parser.add_argument('--password', default=os.environ.get('MIST_RABBITMQ_PASSWORD', ''))
    parser.add_argument('--socket-timeout', type=int, default=None,
                        help='RabbitMQ socket timeout, set to 15-60 on bad connections.')
    parser.add_argument('--exchange', default='mistx',
                        help='The exchange to use for sniffing messages.')

    parser.add_argument('--cloud', default=False, action='store_true',
                        help='Sniff messages destined to the cloud.')
    parser.add_argument('--mist', default=False, action='store_true',
                        help='Sniff messages destined to the mist.')

    parser.add_argument('--gateway', type=arg_hex2int,
                        help='The gateway from which the messages should be sniffed from, defaults to all.')
    parser.add_argument('--queue', default=None,
                        help='Name of the sniffer queue, set it to override the automatically generated name.')
    parser.add_argument('--noverify', default=False, action='store_true',
                        help='Do not verify the certificate of the server.')
    parser.add_argument('-v', '--verbose', default=False, action='store_true',
                        help='Print out more information about sniffed messages.')
    args = parser.parse_args()

    if args.verbose:
        global verbose
        verbose = True

    # Sniff for a specific GW or all of them
    if args.gateway is None:
        gateway = '*'
    else:
        gateway = f'{args.gateway:016X}'

    # Determine sniffing direction
    if args.cloud is False and args.mist is False:
        print("Please specify --mist, --cloud or both!")
        return

    rkeys = []
    if args.cloud:
        rkeys.append(f'cloud.{gateway}.*')

    if args.mist:
        rkeys.append(f'mist.{gateway}.*')

    # Set up a connection
    if args.noverify:
        print('Certificate will not be checked for validity!')
        context = ssl.SSLContext()
        context.verify_mode = ssl.CERT_NONE
        sslo = pika.SSLOptions(context)
    else:
        sslo = None

    pcp = pika.ConnectionParameters(host=args.server,
                                    credentials=pika.PlainCredentials(args.username, args.password),
                                    ssl_options=sslo)
    connection = pika.BlockingConnection(pcp)

    channel = connection.channel()

    # Allow queue name to be customized
    qn = args.queue
    if qn is None:
        qn = f'mist-sniffer-{socket.gethostname()}-{gateway}'

    qdresult = channel.queue_declare(queue=qn, auto_delete=True)
    qname = qdresult.method.queue

    for rkey in rkeys:
        channel.queue_bind(queue=qname, exchange=args.exchange, routing_key=rkey)

    channel.basic_consume(qname, message_received)

    print('Sniffing, press CTRL+C to exit...')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()


if __name__ == '__main__':
    main()
