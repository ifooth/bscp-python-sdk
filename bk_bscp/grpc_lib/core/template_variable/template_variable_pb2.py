# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/template-variable/template_variable.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;pkg/protocol/core/template-variable/template_variable.proto\x12\x04pbtv\x1a!pkg/protocol/core/base/base.proto\"\xa2\x01\n\x10TemplateVariable\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\x04spec\x18\x02 \x01(\x0b\x32\x1a.pbtv.TemplateVariableSpec\x12\x34\n\nattachment\x18\x03 \x01(\x0b\x32 .pbtv.TemplateVariableAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\"U\n\x14TemplateVariableSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65\x66\x61ult_val\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\",\n\x1aTemplateVariableAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\rBbZ`github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-variable;pbtvb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.template_variable.template_variable_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z`github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-variable;pbtv'
  _globals['_TEMPLATEVARIABLE']._serialized_start=105
  _globals['_TEMPLATEVARIABLE']._serialized_end=267
  _globals['_TEMPLATEVARIABLESPEC']._serialized_start=269
  _globals['_TEMPLATEVARIABLESPEC']._serialized_end=354
  _globals['_TEMPLATEVARIABLEATTACHMENT']._serialized_start=356
  _globals['_TEMPLATEVARIABLEATTACHMENT']._serialized_end=400
# @@protoc_insertion_point(module_scope)