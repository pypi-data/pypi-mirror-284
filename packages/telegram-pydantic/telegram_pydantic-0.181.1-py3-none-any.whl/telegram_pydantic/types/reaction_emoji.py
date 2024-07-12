from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionEmoji(BaseModel):
    """
    types.ReactionEmoji
    ID: 0x1b2286b8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionEmoji'] = pydantic.Field(
        'types.ReactionEmoji',
        alias='_'
    )

    emoticon: str
