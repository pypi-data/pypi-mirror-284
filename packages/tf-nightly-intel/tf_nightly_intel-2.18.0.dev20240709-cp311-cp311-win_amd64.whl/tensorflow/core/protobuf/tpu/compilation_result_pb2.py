# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tpu/compilation_result.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.compiler.xla.service import hlo_pb2 as xla_dot_service_dot_hlo__pb2
from tensorflow.core.protobuf import error_codes_pb2 as tensorflow_dot_core_dot_protobuf_dot_error__codes__pb2
try:
  tsl_dot_protobuf_dot_error__codes__pb2 = tensorflow_dot_core_dot_protobuf_dot_error__codes__pb2.tsl_dot_protobuf_dot_error__codes__pb2
except AttributeError:
  tsl_dot_protobuf_dot_error__codes__pb2 = tensorflow_dot_core_dot_protobuf_dot_error__codes__pb2.tsl.protobuf.error_codes_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5tensorflow/core/protobuf/tpu/compilation_result.proto\x12\x0etensorflow.tpu\x1a\x15xla/service/hlo.proto\x1a*tensorflow/core/protobuf/error_codes.proto\"\xf9\x01\n\x16\x43ompilationResultProto\x12+\n\x0bstatus_code\x18\x01 \x01(\x0e\x32\x16.tensorflow.error.Code\x12\x1c\n\x14status_error_message\x18\x02 \x01(\t\x12!\n\nhlo_protos\x18\x03 \x03(\x0b\x32\r.xla.HloProto\x12\x44\n\nerror_code\x18\x04 \x01(\x0e\x32\x30.tensorflow.tpu.CompilationResultProto.ErrorCode\"+\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rOUT_OF_MEMORY\x10\x01\x42\x03\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tensorflow.core.protobuf.tpu.compilation_result_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _COMPILATIONRESULTPROTO._serialized_start=141
  _COMPILATIONRESULTPROTO._serialized_end=390
  _COMPILATIONRESULTPROTO_ERRORCODE._serialized_start=347
  _COMPILATIONRESULTPROTO_ERRORCODE._serialized_end=390
# @@protoc_insertion_point(module_scope)
