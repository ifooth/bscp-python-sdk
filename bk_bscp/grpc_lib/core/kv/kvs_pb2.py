# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/kv/kvs.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as pkg_dot_protocol_dot_core_dot_content_dot_content__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1epkg/protocol/core/kv/kvs.proto\x12\x04pbkv\x1a!pkg/protocol/core/base/base.proto\x1a\'pkg/protocol/core/content/content.proto\"\xb8\x01\n\x02Kv\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08kv_state\x18\x02 \x01(\t\x12\x1a\n\x04spec\x18\x03 \x01(\x0b\x32\x0c.pbkv.KvSpec\x12&\n\nattachment\x18\x04 \x01(\x0b\x32\x12.pbkv.KvAttachment\x12\"\n\x08revision\x18\x05 \x01(\x0b\x32\x10.pbbase.Revision\x12,\n\x0c\x63ontent_spec\x18\x06 \x01(\x0b\x32\x16.pbcontent.ContentSpec\"C\n\x06KvSpec\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0f\n\x07kv_type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\".\n\x0cKvAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\rBSZQgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/kv;pbkvb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.kv.kvs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZQgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/kv;pbkv'
  _globals['_KV']._serialized_start=117
  _globals['_KV']._serialized_end=301
  _globals['_KVSPEC']._serialized_start=303
  _globals['_KVSPEC']._serialized_end=370
  _globals['_KVATTACHMENT']._serialized_start=372
  _globals['_KVATTACHMENT']._serialized_end=418
# @@protoc_insertion_point(module_scope)
