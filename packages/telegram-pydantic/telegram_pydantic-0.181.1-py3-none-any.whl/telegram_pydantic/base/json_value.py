from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# JSONValue - Layer 181
JSONValue = typing.Annotated[
    typing.Union[
        types.JsonArray,
        types.JsonBool,
        types.JsonNull,
        types.JsonNumber,
        types.JsonObject,
        types.JsonString
    ],
    pydantic.Field(discriminator='QUALNAME')
]
