from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonString(BaseModel):
    """
    types.JsonString
    ID: 0xb71e767a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonString'] = pydantic.Field(
        'types.JsonString',
        alias='_'
    )

    value: str
