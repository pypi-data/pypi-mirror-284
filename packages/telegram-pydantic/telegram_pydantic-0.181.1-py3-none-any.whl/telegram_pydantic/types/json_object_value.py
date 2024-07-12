from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonObjectValue(BaseModel):
    """
    types.JsonObjectValue
    ID: 0xc0de1bd9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonObjectValue'] = pydantic.Field(
        'types.JsonObjectValue',
        alias='_'
    )

    key: str
    value: "base.JSONValue"
