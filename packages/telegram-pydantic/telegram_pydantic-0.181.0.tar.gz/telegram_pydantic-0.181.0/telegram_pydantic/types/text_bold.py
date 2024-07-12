from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextBold(BaseModel):
    """
    types.TextBold
    ID: 0x6724abc4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextBold'] = pydantic.Field(
        'types.TextBold',
        alias='_'
    )

    text: "base.RichText"
