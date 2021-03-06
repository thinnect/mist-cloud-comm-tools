# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mist.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mist.proto',
  package='mist',
  syntax='proto3',
  serialized_options=b'Z\"bitbucket.org/thinnect/mist-daemon',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmist.proto\x12\x04mist\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcc\x01\n\x0bMistMessage\x12\x0f\n\x07gateway\x18\x01 \x01(\x06\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\x06\x12\x0e\n\x06source\x18\x03 \x01(\x06\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x12\x0c\n\x04\x61mid\x18\x05 \x01(\r\x12\x0c\n\x04rssi\x18\x06 \x01(\x05\x12\x0b\n\x03lqi\x18\x07 \x01(\r\x12\r\n\x05group\x18\x08 \x01(\r\x12\x0f\n\x07\x63hannel\x18\t \x01(\r\x12-\n\ttimestamp\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB$Z\"bitbucket.org/thinnect/mist-daemonb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_MISTMESSAGE = _descriptor.Descriptor(
  name='MistMessage',
  full_name='mist.MistMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gateway', full_name='mist.MistMessage.gateway', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination', full_name='mist.MistMessage.destination', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='mist.MistMessage.source', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='mist.MistMessage.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amid', full_name='mist.MistMessage.amid', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='mist.MistMessage.rssi', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lqi', full_name='mist.MistMessage.lqi', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='mist.MistMessage.group', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='mist.MistMessage.channel', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mist.MistMessage.timestamp', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=258,
)

_MISTMESSAGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['MistMessage'] = _MISTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MistMessage = _reflection.GeneratedProtocolMessageType('MistMessage', (_message.Message,), {
  'DESCRIPTOR' : _MISTMESSAGE,
  '__module__' : 'mist_pb2'
  # @@protoc_insertion_point(class_scope:mist.MistMessage)
  })
_sym_db.RegisterMessage(MistMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
