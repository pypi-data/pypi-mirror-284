from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JsonNull(BaseModel):
    """
    types.JsonNull
    ID: 0x3f6d7b68
    Layer: 181
    """
    QUALNAME: typing.Literal['types.JsonNull'] = pydantic.Field(
        'types.JsonNull',
        alias='_'
    )

