# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.storage.v1",
    manifest={
        "AvroSchema",
        "AvroRows",
        "AvroSerializationOptions",
    },
)


class AvroSchema(proto.Message):
    r"""Avro schema.

    Attributes:
        schema (str):
            Json serialized schema, as described at
            https://avro.apache.org/docs/1.8.1/spec.html.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AvroRows(proto.Message):
    r"""Avro rows.

    Attributes:
        serialized_binary_rows (bytes):
            Binary serialized rows in a block.
        row_count (int):
            [Deprecated] The count of rows in the returning block.
            Please use the format-independent ReadRowsResponse.row_count
            instead.
    """

    serialized_binary_rows: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class AvroSerializationOptions(proto.Message):
    r"""Contains options specific to Avro Serialization.

    Attributes:
        enable_display_name_attribute (bool):
            Enable displayName attribute in Avro schema.

            The Avro specification requires field names to
            be alphanumeric.  By default, in cases when
            column names do not conform to these
            requirements (e.g. non-ascii unicode codepoints)
            and Avro is requested as an output format, the
            CreateReadSession call will fail.

            Setting this field to true, populates avro field
            names with a placeholder value and populates a
            "displayName" attribute for every avro field
            with the original column name.
    """

    enable_display_name_attribute: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
