# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/credential-scope/credential-scope.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9pkg/protocol/core/credential-scope/credential-scope.proto\x12\x05pbcrs\x1a!pkg/protocol/core/base/base.proto\"B\n\x19\x43redentialScopeAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x15\n\rcredential_id\x18\x02 \x01(\r\"\xa5\x01\n\x13\x43redentialScopeList\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x04spec\x18\x02 \x01(\x0b\x32\x1a.pbcrs.CredentialScopeSpec\x12\x34\n\nattachment\x18\x03 \x01(\x0b\x32 .pbcrs.CredentialScopeAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\"1\n\x13\x43redentialScopeSpec\x12\x0b\n\x03\x61pp\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\"9\n\x0fUpdateScopeSpec\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03\x61pp\x18\x02 \x01(\t\x12\r\n\x05scope\x18\x03 \x01(\tBbZ`github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/credential-scope;pbcrsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.credential_scope.credential_scope_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z`github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/credential-scope;pbcrs'
  _globals['_CREDENTIALSCOPEATTACHMENT']._serialized_start=103
  _globals['_CREDENTIALSCOPEATTACHMENT']._serialized_end=169
  _globals['_CREDENTIALSCOPELIST']._serialized_start=172
  _globals['_CREDENTIALSCOPELIST']._serialized_end=337
  _globals['_CREDENTIALSCOPESPEC']._serialized_start=339
  _globals['_CREDENTIALSCOPESPEC']._serialized_end=388
  _globals['_UPDATESCOPESPEC']._serialized_start=390
  _globals['_UPDATESCOPESPEC']._serialized_end=447
# @@protoc_insertion_point(module_scope)