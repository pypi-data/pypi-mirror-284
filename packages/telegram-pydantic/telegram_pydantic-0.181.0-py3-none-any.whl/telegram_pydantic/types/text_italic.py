from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextItalic(BaseModel):
    """
    types.TextItalic
    ID: 0xd912a59c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextItalic'] = pydantic.Field(
        'types.TextItalic',
        alias='_'
    )

    text: "base.RichText"
