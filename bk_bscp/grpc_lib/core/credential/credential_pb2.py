# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/credential/credential.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-pkg/protocol/core/credential/credential.proto\x12\x0cpbcredential\x1a!pkg/protocol/core/base/base.proto\"\xbf\x01\n\x0e\x43redentialList\x12\n\n\x02id\x18\x01 \x01(\r\x12*\n\x04spec\x18\x02 \x01(\x0b\x32\x1c.pbcredential.CredentialSpec\x12\x36\n\nattachment\x18\x03 \x01(\x0b\x32\".pbcredential.CredentialAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\x12\x19\n\x11\x63redential_scopes\x18\x05 \x03(\t\"\x84\x01\n\x0e\x43redentialSpec\x12\x17\n\x0f\x63redential_type\x18\x01 \x01(\t\x12\x16\n\x0e\x65nc_credential\x18\x02 \x01(\t\x12\x15\n\renc_algorithm\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0e\n\x06\x65nable\x18\x06 \x01(\x08\"&\n\x14\x43redentialAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\" \n\x0f\x43redentialScope\x12\r\n\x05scope\x18\x01 \x01(\tBcZagithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/credential;pbcredentialb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.credential.credential_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Zagithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/credential;pbcredential'
  _globals['_CREDENTIALLIST']._serialized_start=99
  _globals['_CREDENTIALLIST']._serialized_end=290
  _globals['_CREDENTIALSPEC']._serialized_start=293
  _globals['_CREDENTIALSPEC']._serialized_end=425
  _globals['_CREDENTIALATTACHMENT']._serialized_start=427
  _globals['_CREDENTIALATTACHMENT']._serialized_end=465
  _globals['_CREDENTIALSCOPE']._serialized_start=467
  _globals['_CREDENTIALSCOPE']._serialized_end=499
# @@protoc_insertion_point(module_scope)
