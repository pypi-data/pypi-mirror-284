# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Radio.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import LabelVisibilityMessage_pb2 as streamlit_dot_proto_dot_LabelVisibilityMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreamlit/proto/Radio.proto\x1a,streamlit/proto/LabelVisibilityMessage.proto\"\x90\x02\n\x05Radio\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07options\x18\x04 \x03(\t\x12\x0c\n\x04help\x18\x05 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x06 \x01(\t\x12\x12\n\x05value\x18\x07 \x01(\x05H\x01\x88\x01\x01\x12\x11\n\tset_value\x18\x08 \x01(\x08\x12\x10\n\x08\x64isabled\x18\t \x01(\x08\x12\x12\n\nhorizontal\x18\n \x01(\x08\x12\x31\n\x10label_visibility\x18\x0b \x01(\x0b\x32\x17.LabelVisibilityMessage\x12\x10\n\x08\x63\x61ptions\x18\x0c \x03(\tB\n\n\x08_defaultB\x08\n\x06_valueB*\n\x1c\x63om.snowflake.apps.streamlitB\nRadioProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.Radio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.snowflake.apps.streamlitB\nRadioProto'
  _globals['_RADIO']._serialized_start=78
  _globals['_RADIO']._serialized_end=350
# @@protoc_insertion_point(module_scope)
