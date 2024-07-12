from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonObject(BaseModel):
    """
    types.JsonObject
    ID: 0x99c1d49d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonObject'] = pydantic.Field(
        'types.JsonObject',
        alias='_'
    )

    value: list["base.JSONObjectValue"]
