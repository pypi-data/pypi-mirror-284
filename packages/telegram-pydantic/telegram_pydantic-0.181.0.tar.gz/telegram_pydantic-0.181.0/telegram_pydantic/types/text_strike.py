from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextStrike(BaseModel):
    """
    types.TextStrike
    ID: 0x9bf8bb95
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextStrike'] = pydantic.Field(
        'types.TextStrike',
        alias='_'
    )

    text: "base.RichText"
