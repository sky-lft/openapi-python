# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/control/control.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bproto/control/control.proto\x12\x18longbridgeapp.control.v1\"\xd6\x01\n\x05\x43lose\x12\x32\n\x04\x63ode\x18\x01 \x01(\x0e\x32$.longbridgeapp.control.v1.Close.Code\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\x88\x01\n\x04\x43ode\x12\x14\n\x10HeartbeatTimeout\x10\x00\x12\x0f\n\x0bServerError\x10\x01\x12\x12\n\x0eServerShutdown\x10\x02\x12\x0f\n\x0bUnpackError\x10\x03\x12\r\n\tAuthError\x10\x04\x12\x0f\n\x0bSessExpired\x10\x05\x12\x14\n\x10\x43onnectDuplicate\x10\x06\"\x1e\n\tHeartbeat\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"\x1c\n\x0b\x41uthRequest\x12\r\n\x05token\x18\x01 \x01(\t\"3\n\x0c\x41uthResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x03\"&\n\x10ReconnectRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"8\n\x11ReconnectResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x03*L\n\x07\x43ommand\x12\r\n\tCMD_CLOSE\x10\x00\x12\x11\n\rCMD_HEARTBEAT\x10\x01\x12\x0c\n\x08\x43MD_AUTH\x10\x02\x12\x11\n\rCMD_RECONNECT\x10\x03\x62\x06proto3')

_COMMAND = DESCRIPTOR.enum_types_by_name['Command']
Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
CMD_CLOSE = 0
CMD_HEARTBEAT = 1
CMD_AUTH = 2
CMD_RECONNECT = 3


_CLOSE = DESCRIPTOR.message_types_by_name['Close']
_HEARTBEAT = DESCRIPTOR.message_types_by_name['Heartbeat']
_AUTHREQUEST = DESCRIPTOR.message_types_by_name['AuthRequest']
_AUTHRESPONSE = DESCRIPTOR.message_types_by_name['AuthResponse']
_RECONNECTREQUEST = DESCRIPTOR.message_types_by_name['ReconnectRequest']
_RECONNECTRESPONSE = DESCRIPTOR.message_types_by_name['ReconnectResponse']
_CLOSE_CODE = _CLOSE.enum_types_by_name['Code']
Close = _reflection.GeneratedProtocolMessageType('Close', (_message.Message,), {
  'DESCRIPTOR' : _CLOSE,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.Close)
  })
_sym_db.RegisterMessage(Close)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.Heartbeat)
  })
_sym_db.RegisterMessage(Heartbeat)

AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUEST,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.AuthRequest)
  })
_sym_db.RegisterMessage(AuthRequest)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESPONSE,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.AuthResponse)
  })
_sym_db.RegisterMessage(AuthResponse)

ReconnectRequest = _reflection.GeneratedProtocolMessageType('ReconnectRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECONNECTREQUEST,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.ReconnectRequest)
  })
_sym_db.RegisterMessage(ReconnectRequest)

ReconnectResponse = _reflection.GeneratedProtocolMessageType('ReconnectResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECONNECTRESPONSE,
  '__module__' : 'proto.control.control_pb2'
  # @@protoc_insertion_point(class_scope:longbridgeapp.control.v1.ReconnectResponse)
  })
_sym_db.RegisterMessage(ReconnectResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMAND._serialized_start=487
  _COMMAND._serialized_end=563
  _CLOSE._serialized_start=58
  _CLOSE._serialized_end=272
  _CLOSE_CODE._serialized_start=136
  _CLOSE_CODE._serialized_end=272
  _HEARTBEAT._serialized_start=274
  _HEARTBEAT._serialized_end=304
  _AUTHREQUEST._serialized_start=306
  _AUTHREQUEST._serialized_end=334
  _AUTHRESPONSE._serialized_start=336
  _AUTHRESPONSE._serialized_end=387
  _RECONNECTREQUEST._serialized_start=389
  _RECONNECTREQUEST._serialized_end=427
  _RECONNECTRESPONSE._serialized_start=429
  _RECONNECTRESPONSE._serialized_end=485
# @@protoc_insertion_point(module_scope)