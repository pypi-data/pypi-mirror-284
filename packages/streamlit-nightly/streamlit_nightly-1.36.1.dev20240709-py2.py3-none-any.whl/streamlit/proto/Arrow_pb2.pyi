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
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Arrow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EditingMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EditingModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Arrow._EditingMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        READ_ONLY: Arrow._EditingMode.ValueType  # 0
        """Read-only table."""
        FIXED: Arrow._EditingMode.ValueType  # 1
        """Activates editing but only allow editing of existing cells."""
        DYNAMIC: Arrow._EditingMode.ValueType  # 2
        """Activates editing and allow adding & deleting rows."""

    class EditingMode(_EditingMode, metaclass=_EditingModeEnumTypeWrapper):
        """Available editing modes:"""

    READ_ONLY: Arrow.EditingMode.ValueType  # 0
    """Read-only table."""
    FIXED: Arrow.EditingMode.ValueType  # 1
    """Activates editing but only allow editing of existing cells."""
    DYNAMIC: Arrow.EditingMode.ValueType  # 2
    """Activates editing and allow adding & deleting rows."""

    class _SelectionMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SelectionModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Arrow._SelectionMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SINGLE_ROW: Arrow._SelectionMode.ValueType  # 0
        """Only one row can be selected at a time."""
        MULTI_ROW: Arrow._SelectionMode.ValueType  # 1
        """Multiple rows can be selected at a time."""
        SINGLE_COLUMN: Arrow._SelectionMode.ValueType  # 2
        """Only one column can be selected at a time."""
        MULTI_COLUMN: Arrow._SelectionMode.ValueType  # 3
        """Multiple columns can be selected at a time."""

    class SelectionMode(_SelectionMode, metaclass=_SelectionModeEnumTypeWrapper):
        """Available editing modes:"""

    SINGLE_ROW: Arrow.SelectionMode.ValueType  # 0
    """Only one row can be selected at a time."""
    MULTI_ROW: Arrow.SelectionMode.ValueType  # 1
    """Multiple rows can be selected at a time."""
    SINGLE_COLUMN: Arrow.SelectionMode.ValueType  # 2
    """Only one column can be selected at a time."""
    MULTI_COLUMN: Arrow.SelectionMode.ValueType  # 3
    """Multiple columns can be selected at a time."""

    DATA_FIELD_NUMBER: builtins.int
    STYLER_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    USE_CONTAINER_WIDTH_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    COLUMNS_FIELD_NUMBER: builtins.int
    EDITING_MODE_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    FORM_ID_FIELD_NUMBER: builtins.int
    COLUMN_ORDER_FIELD_NUMBER: builtins.int
    SELECTION_MODE_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """The serialized arrow dataframe"""
    width: builtins.int
    """Width in pixels"""
    height: builtins.int
    """Height in pixels"""
    use_container_width: builtins.bool
    """If True, will overwrite the dataframe width to fit to container."""
    id: builtins.str
    """The id of the widget, this is required if the dataframe is editable"""
    columns: builtins.str
    """Column configuration as JSON"""
    editing_mode: global___Arrow.EditingMode.ValueType
    """Activate table editing"""
    disabled: builtins.bool
    """Deactivates editing"""
    form_id: builtins.str
    """The form ID of the widget, this is required if the dataframe is editable"""
    @property
    def styler(self) -> global___Styler:
        """Pandas styler information"""

    @property
    def column_order(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Defines the order in which columns are displayed"""

    @property
    def selection_mode(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Arrow.SelectionMode.ValueType]:
        """Activated dataframe selections events"""

    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
        styler: global___Styler | None = ...,
        width: builtins.int = ...,
        height: builtins.int = ...,
        use_container_width: builtins.bool = ...,
        id: builtins.str = ...,
        columns: builtins.str = ...,
        editing_mode: global___Arrow.EditingMode.ValueType = ...,
        disabled: builtins.bool = ...,
        form_id: builtins.str = ...,
        column_order: collections.abc.Iterable[builtins.str] | None = ...,
        selection_mode: collections.abc.Iterable[global___Arrow.SelectionMode.ValueType] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["styler", b"styler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["column_order", b"column_order", "columns", b"columns", "data", b"data", "disabled", b"disabled", "editing_mode", b"editing_mode", "form_id", b"form_id", "height", b"height", "id", b"id", "selection_mode", b"selection_mode", "styler", b"styler", "use_container_width", b"use_container_width", "width", b"width"]) -> None: ...

global___Arrow = Arrow

@typing.final
class Styler(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    CAPTION_FIELD_NUMBER: builtins.int
    STYLES_FIELD_NUMBER: builtins.int
    DISPLAY_VALUES_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    """The Styler's source UUID (if the user provided one), or the path-based
    hash that we generate (if no source UUID was provided).
    """
    caption: builtins.str
    """The table's caption."""
    styles: builtins.str
    """`styles` contains the CSS for the entire source table."""
    display_values: builtins.bytes
    """display_values is another ArrowTable: a copy of the source table, but
    with all the display values formatted to the user-specified rules.
    """
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        caption: builtins.str = ...,
        styles: builtins.str = ...,
        display_values: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["caption", b"caption", "display_values", b"display_values", "styles", b"styles", "uuid", b"uuid"]) -> None: ...

global___Styler = Styler
