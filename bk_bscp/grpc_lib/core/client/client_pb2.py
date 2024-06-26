# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/client/client.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%pkg/protocol/core/client/client.proto\x12\x08pbclient\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"~\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\r\x12\"\n\x04spec\x18\x02 \x01(\x0b\x32\x14.pbclient.ClientSpec\x12.\n\nattachment\x18\x03 \x01(\x0b\x32\x1a.pbclient.ClientAttachment\x12\x14\n\x0cmessage_type\x18\x04 \x01(\t\"\xf6\x03\n\nClientSpec\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x01(\t\x12\x13\n\x0b\x61nnotations\x18\x04 \x01(\t\x12\x36\n\x12\x66irst_connect_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x13last_heartbeat_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\ronline_status\x18\x07 \x01(\t\x12*\n\x08resource\x18\x08 \x01(\x0b\x32\x18.pbclient.ClientResource\x12\x1a\n\x12\x63urrent_release_id\x18\t \x01(\r\x12\x19\n\x11target_release_id\x18\n \x01(\r\x12\x1d\n\x15release_change_status\x18\x0b \x01(\t\x12$\n\x1crelease_change_failed_reason\x18\x0c \x01(\t\x12\x1c\n\x14\x66\x61iled_detail_reason\x18\r \x01(\t\x12\x13\n\x0b\x63lient_type\x18\x0e \x01(\t\x12\x1c\n\x14\x63urrent_release_name\x18\x0f \x01(\t\x12\x1e\n\x16specific_failed_reason\x18\x10 \x01(\t\"?\n\x10\x43lientAttachment\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0e\n\x06\x62iz_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\r\"\xcc\x01\n\x0e\x43lientResource\x12\x11\n\tcpu_usage\x18\x01 \x01(\x01\x12\x15\n\rcpu_max_usage\x18\x02 \x01(\x01\x12\x15\n\rcpu_min_usage\x18\x03 \x01(\x01\x12\x15\n\rcpu_avg_usage\x18\x04 \x01(\x01\x12\x14\n\x0cmemory_usage\x18\x05 \x01(\x04\x12\x18\n\x10memory_max_usage\x18\x06 \x01(\x04\x12\x18\n\x10memory_min_usage\x18\x07 \x01(\x04\x12\x18\n\x10memory_avg_usage\x18\x08 \x01(\x04\"\xa3\x02\n\x14\x43lientQueryCondition\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12&\n\x05label\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1c\n\x14\x63urrent_release_name\x18\x04 \x01(\t\x12\x1b\n\x13target_release_name\x18\x05 \x01(\t\x12\x1d\n\x15release_change_status\x18\x06 \x03(\t\x12,\n\x0b\x61nnotations\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\ronline_status\x18\x08 \x03(\t\x12\x16\n\x0e\x63lient_version\x18\t \x01(\t\x12\x13\n\x0b\x63lient_type\x18\n \x01(\t\"\x91\x01\n\x0f\x43lientCommonReq\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12.\n\x06search\x18\x03 \x01(\x0b\x32\x1e.pbclient.ClientQueryCondition\x12\x1b\n\x13last_heartbeat_time\x18\x04 \x01(\x03\x12\x11\n\tpull_time\x18\x05 \x01(\x03\x42[ZYgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/client;pbclientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.client.client_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZYgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/client;pbclient'
  _globals['_CLIENT']._serialized_start=114
  _globals['_CLIENT']._serialized_end=240
  _globals['_CLIENTSPEC']._serialized_start=243
  _globals['_CLIENTSPEC']._serialized_end=745
  _globals['_CLIENTATTACHMENT']._serialized_start=747
  _globals['_CLIENTATTACHMENT']._serialized_end=810
  _globals['_CLIENTRESOURCE']._serialized_start=813
  _globals['_CLIENTRESOURCE']._serialized_end=1017
  _globals['_CLIENTQUERYCONDITION']._serialized_start=1020
  _globals['_CLIENTQUERYCONDITION']._serialized_end=1311
  _globals['_CLIENTCOMMONREQ']._serialized_start=1314
  _globals['_CLIENTCOMMONREQ']._serialized_end=1459
# @@protoc_insertion_point(module_scope)
