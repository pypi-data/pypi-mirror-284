from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonNumber(BaseModel):
    """
    types.JsonNumber
    ID: 0x2be0dfa4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonNumber'] = pydantic.Field(
        'types.JsonNumber',
        alias='_'
    )

    value: float
