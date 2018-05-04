# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CMN_MAPI.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CMN_MAPI.proto',
  package='CMN_MAPI',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x43MN_MAPI.proto\x12\x08\x43MN_MAPI\"p\n\x06Header\x12\r\n\x05token\x18\x01 \x01(\r\x12\x10\n\x08\x65rr_code\x18\x02 \x01(\r\x12\x0f\n\x07\x65rr_msg\x18\x03 \x01(\t\x12\x0f\n\x07sess_id\x18\x04 \x01(\r\x12\x11\n\x06offset\x18\x05 \x01(\r:\x01\x30\x12\x10\n\x05limit\x18\x06 \x01(\r:\x01\x30\"+\n\x07Msg_Ack\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header\"1\n\rMsg_StatusGet\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header\".\n\nMsg_Status\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header\"S\n\x10Msg_LogConfigure\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header\x12\x0e\n\x06\x65nable\x18\x02 \x02(\x08\x12\r\n\x05level\x18\x03 \x02(\r\"+\n\x07Msg_Log\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header\"0\n\x0cMsg_Shutdown\x12 \n\x06header\x18\x01 \x02(\x0b\x32\x10.CMN_MAPI.Header*\x12\n\x08Protocol\x12\x06\n\x02ID\x10\x01')
)

_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='CMN_MAPI.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ID', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=466,
  serialized_end=484,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOL)

Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
ID = 1



_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='CMN_MAPI.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='CMN_MAPI.Header.token', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='CMN_MAPI.Header.err_code', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='CMN_MAPI.Header.err_msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sess_id', full_name='CMN_MAPI.Header.sess_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='CMN_MAPI.Header.offset', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='CMN_MAPI.Header.limit', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=140,
)


_MSG_ACK = _descriptor.Descriptor(
  name='Msg_Ack',
  full_name='CMN_MAPI.Msg_Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_Ack.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=185,
)


_MSG_STATUSGET = _descriptor.Descriptor(
  name='Msg_StatusGet',
  full_name='CMN_MAPI.Msg_StatusGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_StatusGet.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=236,
)


_MSG_STATUS = _descriptor.Descriptor(
  name='Msg_Status',
  full_name='CMN_MAPI.Msg_Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_Status.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=284,
)


_MSG_LOGCONFIGURE = _descriptor.Descriptor(
  name='Msg_LogConfigure',
  full_name='CMN_MAPI.Msg_LogConfigure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_LogConfigure.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='CMN_MAPI.Msg_LogConfigure.enable', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='CMN_MAPI.Msg_LogConfigure.level', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=369,
)


_MSG_LOG = _descriptor.Descriptor(
  name='Msg_Log',
  full_name='CMN_MAPI.Msg_Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_Log.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=414,
)


_MSG_SHUTDOWN = _descriptor.Descriptor(
  name='Msg_Shutdown',
  full_name='CMN_MAPI.Msg_Shutdown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='CMN_MAPI.Msg_Shutdown.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=464,
)

_MSG_ACK.fields_by_name['header'].message_type = _HEADER
_MSG_STATUSGET.fields_by_name['header'].message_type = _HEADER
_MSG_STATUS.fields_by_name['header'].message_type = _HEADER
_MSG_LOGCONFIGURE.fields_by_name['header'].message_type = _HEADER
_MSG_LOG.fields_by_name['header'].message_type = _HEADER
_MSG_SHUTDOWN.fields_by_name['header'].message_type = _HEADER
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Msg_Ack'] = _MSG_ACK
DESCRIPTOR.message_types_by_name['Msg_StatusGet'] = _MSG_STATUSGET
DESCRIPTOR.message_types_by_name['Msg_Status'] = _MSG_STATUS
DESCRIPTOR.message_types_by_name['Msg_LogConfigure'] = _MSG_LOGCONFIGURE
DESCRIPTOR.message_types_by_name['Msg_Log'] = _MSG_LOG
DESCRIPTOR.message_types_by_name['Msg_Shutdown'] = _MSG_SHUTDOWN
DESCRIPTOR.enum_types_by_name['Protocol'] = _PROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Header)
  ))
_sym_db.RegisterMessage(Header)

Msg_Ack = _reflection.GeneratedProtocolMessageType('Msg_Ack', (_message.Message,), dict(
  DESCRIPTOR = _MSG_ACK,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_Ack)
  ))
_sym_db.RegisterMessage(Msg_Ack)

Msg_StatusGet = _reflection.GeneratedProtocolMessageType('Msg_StatusGet', (_message.Message,), dict(
  DESCRIPTOR = _MSG_STATUSGET,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_StatusGet)
  ))
_sym_db.RegisterMessage(Msg_StatusGet)

Msg_Status = _reflection.GeneratedProtocolMessageType('Msg_Status', (_message.Message,), dict(
  DESCRIPTOR = _MSG_STATUS,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_Status)
  ))
_sym_db.RegisterMessage(Msg_Status)

Msg_LogConfigure = _reflection.GeneratedProtocolMessageType('Msg_LogConfigure', (_message.Message,), dict(
  DESCRIPTOR = _MSG_LOGCONFIGURE,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_LogConfigure)
  ))
_sym_db.RegisterMessage(Msg_LogConfigure)

Msg_Log = _reflection.GeneratedProtocolMessageType('Msg_Log', (_message.Message,), dict(
  DESCRIPTOR = _MSG_LOG,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_Log)
  ))
_sym_db.RegisterMessage(Msg_Log)

Msg_Shutdown = _reflection.GeneratedProtocolMessageType('Msg_Shutdown', (_message.Message,), dict(
  DESCRIPTOR = _MSG_SHUTDOWN,
  __module__ = 'CMN_MAPI_pb2'
  # @@protoc_insertion_point(class_scope:CMN_MAPI.Msg_Shutdown)
  ))
_sym_db.RegisterMessage(Msg_Shutdown)


# @@protoc_insertion_point(module_scope)
