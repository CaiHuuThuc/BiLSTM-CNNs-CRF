# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\"\x17\n\x03Req\x12\x10\n\x08sentence\x18\x01 \x01(\t\"#\n\x03Res\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t2^\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x12\x16\n\x06getNER\x12\x04.Req\x1a\x04.Res\"\x00\x12\x16\n\x06getPOS\x12\x04.Req\x1a\x04.Res\"\x00\x62\x06proto3')
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=43,
)


_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentence', full_name='Req.sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=45,
  serialized_end=68,
)


_RES = _descriptor.Descriptor(
  name='Res',
  full_name='Res',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='Res.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='Res.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=70,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['Req'] = _REQ
DESCRIPTOR.message_types_by_name['Res'] = _RES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), dict(
  DESCRIPTOR = _NUMBER,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  ))
_sym_db.RegisterMessage(Number)

Req = _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), dict(
  DESCRIPTOR = _REQ,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Req)
  ))
_sym_db.RegisterMessage(Req)

Res = _reflection.GeneratedProtocolMessageType('Res', (_message.Message,), dict(
  DESCRIPTOR = _RES,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Res)
  ))
_sym_db.RegisterMessage(Res)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=107,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getNER',
    full_name='Calculator.getNER',
    index=1,
    containing_service=None,
    input_type=_REQ,
    output_type=_RES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getPOS',
    full_name='Calculator.getPOS',
    index=2,
    containing_service=None,
    input_type=_REQ,
    output_type=_RES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
