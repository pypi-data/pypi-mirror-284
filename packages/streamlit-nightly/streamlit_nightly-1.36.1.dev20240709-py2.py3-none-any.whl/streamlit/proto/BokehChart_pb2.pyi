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
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BokehChart(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIGURE_FIELD_NUMBER: builtins.int
    USE_CONTAINER_WIDTH_FIELD_NUMBER: builtins.int
    ELEMENT_ID_FIELD_NUMBER: builtins.int
    figure: builtins.str
    """A JSON-formatted string from the Bokeh chart figure."""
    use_container_width: builtins.bool
    """If True, will overwrite the chart width spec to fit to container."""
    element_id: builtins.str
    """A unique ID of this element."""
    def __init__(
        self,
        *,
        figure: builtins.str = ...,
        use_container_width: builtins.bool = ...,
        element_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["element_id", b"element_id", "figure", b"figure", "use_container_width", b"use_container_width"]) -> None: ...

global___BokehChart = BokehChart
