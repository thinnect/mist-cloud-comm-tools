# mist-cloud-comm-tools

Basic development and debugging tools for interacting with the Mist AMQP broker.

## Tools

### mist-cloud-sender

The sender can be used send messages into the message exchange. The message
can be constructed for any source / gateway / destination and direction.

Send a message to the cloud from 0000000000000001 to 0015001500150015
through 1122334455667788:

```
mist-cloud-sender --cloud -w 1122334455667788
                  -s 0000000000000001 -d 0015001500150015
                  -m 3fEE -p AABBCCDD`
```

Send a message to the mist to 0000000000000001 from 0015001500150015
through 1122334455667788:

```
mist-cloud-sender --mist -w 1122334455667788
                  -s 0015001500150015 -d 0000000000000001
                  -m 3fEE -p AABBCCDD`
```

### mist-cloud-sniffer

The sniffer can be used to listen in on communications. It can be configured
to listen to messages going in either direction.

To sniff messages coming from gateway 1122334455667788 to the cloud:
`mist-cloud-sniffer --gateway 1122334455667788 --cloud`

To sniff messages going to gateway 1122334455667788 from the cloud:
`mist-cloud-sniffer --gateway 1122334455667788 --mist`

## Server and credentials

The tools require access to the AMQP broker, the server, username and password
can be passed on the command line with `--server`, `--username` and `--password`
or set in the environment:
```
export MIST_RABBITMQ_SERVER=sever.somewhere.net
export MIST_RABBITMQ_USER=username
export MIST_RABBITMQ_PASSWORD=password
```
Command-line parameters override the environment values.

## Build the package

Make sure you have an up-to-date PyPA build:
`python3 -m pip install --upgrade build`

Build the package:
`python3 -m build`

Install the package:
`python3 -m pip install dist/mist_cloud_comm_tools-X.Y.Z-py3-none-any.whl`
