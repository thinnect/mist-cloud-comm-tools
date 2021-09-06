#!/usr/bin/env python3
"""
Mist cloud AMQP message sender.
"""

__copyright__ = 'Thinnect Inc. 2021'
__license__ = 'MIT'

import pika
import argparse
import ssl
import os

from google.protobuf.timestamp_pb2 import Timestamp

from .mist_pb2 import MistMessage

from .formatters import format_proto_timestamp
from .parsers import arg_hex2int, arg_hexpayload


def main():

    parser = argparse.ArgumentParser(description='Send mist event data directly to RabbitMQ exchange.')
    parser.add_argument('--server', default=os.environ.get('MIST_RABBITMQ_SERVER', 'server.rabbit.mq'),
                        help='The server to use for sending data')
    parser.add_argument('--username', default=os.environ.get('MIST_RABBITMQ_USERNAME', 'bugsbunny'))
    parser.add_argument('--password', default=os.environ.get('MIST_RABBITMQ_PASSWORD', ''))
    parser.add_argument('--socket-timeout', type=int, default=None,
                        help='RabbitMQ socket timeout, set to 15-60 on bad connections.')
    parser.add_argument('--noverify', default=False, action='store_true',
                        help='Do not verify the certificate of the server.')
    parser.add_argument('--exchange', default='mistx',
                        help='The exchange to use for sniffing messages.')

    parser.add_argument('--cloud', default=False, action='store_true',
                        help='Send the message to the cloud, not mist.')

    parser.add_argument('-s', '--source', default='0015001500150015', type=arg_hex2int,
                        help='The source of the message.')
    parser.add_argument('-d', '--destination', default='FFFFFFFFFFFFFFFF', type=arg_hex2int,
                        help='The destination of the message.')
    parser.add_argument('-w', '--gateway', default='FFFFFFFFFFFFFFFF', type=arg_hex2int,
                        help='The gateway through which the messages should be sent.')
    parser.add_argument('-g', '--group', default='00FF', type=arg_hex2int,
                        help='The extended AM group / PAN ID of the message.')
    parser.add_argument('-m', '--amid', required=True, type=arg_hex2int,
                        help='The extended AMID of the message.')
    parser.add_argument('-p', '--payload', default="", type=arg_hexpayload,
                        help='The payload of the message.')

    args = parser.parse_args()

    if args.cloud:
        rkey = f'cloud.{args.gateway:016X}.{args.destination:016X}'
    else:
        rkey = f'mist.{args.gateway:016X}.{args.destination:016X}'

    mm = MistMessage()
    mm.timestamp.GetCurrentTime()

    mm.destination = args.destination
    mm.source = args.source
    mm.gateway = args.gateway
    mm.group = args.group
    mm.amid = args.amid
    mm.payload = args.payload

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
    channel.basic_publish(exchange=args.exchange, routing_key=rkey, body=mm.SerializeToString())

    print(rkey)

    print(f'@{format_proto_timestamp(mm.timestamp)}'
          f' {{{mm.group:04X}}}{mm.source:016X}->{mm.destination:016X}[{mm.amid:04X}]'
          f' {len(mm.payload):3d}: {mm.payload.hex().upper()}'
          f' {mm.lqi:02X}:{mm.rssi:3d} ({mm.channel:2d})')

    connection.close()


if __name__ == '__main__':
    main()
