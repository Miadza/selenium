# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: example.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'example.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x07\x65xample\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"2\n\x0fGetUserResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"4\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"%\n\x12\x43reateUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"7\n\x11UpdateUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tnew_email\x18\x02 \x01(\t\"%\n\x12UpdateUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"$\n\x11\x44\x65leteUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x12\n\x10ListUsersRequest\"<\n\x11ListUsersResponse\x12\'\n\x05users\x18\x01 \x03(\x0b\x32\x18.example.GetUserResponse2\xe7\x02\n\x0e\x45xampleService\x12<\n\x07GetUser\x12\x17.example.GetUserRequest\x1a\x18.example.GetUserResponse\x12\x45\n\nCreateUser\x12\x1a.example.CreateUserRequest\x1a\x1b.example.CreateUserResponse\x12\x45\n\nUpdateUser\x12\x1a.example.UpdateUserRequest\x1a\x1b.example.UpdateUserResponse\x12\x45\n\nDeleteUser\x12\x1a.example.DeleteUserRequest\x1a\x1b.example.DeleteUserResponse\x12\x42\n\tListUsers\x12\x19.example.ListUsersRequest\x1a\x1a.example.ListUsersResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETUSERREQUEST']._serialized_start=26
  _globals['_GETUSERREQUEST']._serialized_end=59
  _globals['_GETUSERRESPONSE']._serialized_start=61
  _globals['_GETUSERRESPONSE']._serialized_end=111
  _globals['_CREATEUSERREQUEST']._serialized_start=113
  _globals['_CREATEUSERREQUEST']._serialized_end=165
  _globals['_CREATEUSERRESPONSE']._serialized_start=167
  _globals['_CREATEUSERRESPONSE']._serialized_end=204
  _globals['_UPDATEUSERREQUEST']._serialized_start=206
  _globals['_UPDATEUSERREQUEST']._serialized_end=261
  _globals['_UPDATEUSERRESPONSE']._serialized_start=263
  _globals['_UPDATEUSERRESPONSE']._serialized_end=300
  _globals['_DELETEUSERREQUEST']._serialized_start=302
  _globals['_DELETEUSERREQUEST']._serialized_end=338
  _globals['_DELETEUSERRESPONSE']._serialized_start=340
  _globals['_DELETEUSERRESPONSE']._serialized_end=377
  _globals['_LISTUSERSREQUEST']._serialized_start=379
  _globals['_LISTUSERSREQUEST']._serialized_end=397
  _globals['_LISTUSERSRESPONSE']._serialized_start=399
  _globals['_LISTUSERSRESPONSE']._serialized_end=459
  _globals['_EXAMPLESERVICE']._serialized_start=462
  _globals['_EXAMPLESERVICE']._serialized_end=821
# @@protoc_insertion_point(module_scope)
