# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/release/release.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'pkg/protocol/core/release/release.proto\x12\tpbrelease\x1a\x1cgoogle/protobuf/struct.proto\x1a!pkg/protocol/core/base/base.proto\"\xc2\x01\n\x07Release\x12\n\n\x02id\x18\x01 \x01(\r\x12$\n\x04spec\x18\x02 \x01(\x0b\x32\x16.pbrelease.ReleaseSpec\x12(\n\x06status\x18\x03 \x01(\x0b\x32\x18.pbrelease.ReleaseStatus\x12\x30\n\nattachment\x18\x04 \x01(\x0b\x32\x1c.pbrelease.ReleaseAttachment\x12)\n\x08revision\x18\x05 \x01(\x0b\x32\x17.pbbase.CreatedRevision\"R\n\x0bReleaseSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x12\n\ndeprecated\x18\x03 \x01(\x08\x12\x13\n\x0bpublish_num\x18\x04 \x01(\r\"\xb5\x02\n\rReleaseStatus\x12\x16\n\x0epublish_status\x18\x01 \x01(\t\x12?\n\x0freleased_groups\x18\x02 \x03(\x0b\x32&.pbrelease.ReleaseStatus.ReleasedGroup\x12\x16\n\x0e\x66ully_released\x18\x03 \x01(\x08\x1a\xb2\x01\n\rReleasedGroup\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04mode\x18\x03 \x01(\t\x12-\n\x0cold_selector\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12-\n\x0cnew_selector\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03uid\x18\x06 \x01(\t\x12\x0e\n\x06\x65\x64ited\x18\x07 \x01(\x08\"3\n\x11ReleaseAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\rB]Z[github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/release;pbreleaseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.release.release_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z[github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/release;pbrelease'
  _globals['_RELEASE']._serialized_start=120
  _globals['_RELEASE']._serialized_end=314
  _globals['_RELEASESPEC']._serialized_start=316
  _globals['_RELEASESPEC']._serialized_end=398
  _globals['_RELEASESTATUS']._serialized_start=401
  _globals['_RELEASESTATUS']._serialized_end=710
  _globals['_RELEASESTATUS_RELEASEDGROUP']._serialized_start=532
  _globals['_RELEASESTATUS_RELEASEDGROUP']._serialized_end=710
  _globals['_RELEASEATTACHMENT']._serialized_start=712
  _globals['_RELEASEATTACHMENT']._serialized_end=763
# @@protoc_insertion_point(module_scope)
