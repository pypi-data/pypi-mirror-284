from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextPlain(BaseModel):
    """
    types.TextPlain
    ID: 0x744694e0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextPlain'] = pydantic.Field(
        'types.TextPlain',
        alias='_'
    )

    text: str
