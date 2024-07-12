from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonArray(BaseModel):
    """
    types.JsonArray
    ID: 0xf7444763
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonArray'] = pydantic.Field(
        'types.JsonArray',
        alias='_'
    )

    value: list["base.JSONValue"]
