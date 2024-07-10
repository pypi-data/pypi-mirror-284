"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import streamlit.proto.WidgetStates_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ClientState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_STRING_FIELD_NUMBER: builtins.int
    WIDGET_STATES_FIELD_NUMBER: builtins.int
    PAGE_SCRIPT_HASH_FIELD_NUMBER: builtins.int
    PAGE_NAME_FIELD_NUMBER: builtins.int
    FRAGMENT_ID_FIELD_NUMBER: builtins.int
    query_string: builtins.str
    page_script_hash: builtins.str
    page_name: builtins.str
    fragment_id: builtins.str
    @property
    def widget_states(self) -> streamlit.proto.WidgetStates_pb2.WidgetStates: ...
    def __init__(
        self,
        *,
        query_string: builtins.str = ...,
        widget_states: streamlit.proto.WidgetStates_pb2.WidgetStates | None = ...,
        page_script_hash: builtins.str = ...,
        page_name: builtins.str = ...,
        fragment_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["widget_states", b"widget_states"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["fragment_id", b"fragment_id", "page_name", b"page_name", "page_script_hash", b"page_script_hash", "query_string", b"query_string", "widget_states", b"widget_states"]) -> None: ...

global___ClientState = ClientState
