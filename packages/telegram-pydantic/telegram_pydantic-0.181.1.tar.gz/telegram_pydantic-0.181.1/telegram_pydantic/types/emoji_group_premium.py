from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupPremium(BaseModel):
    """
    types.EmojiGroupPremium
    ID: 0x93bcf34
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiGroupPremium'] = pydantic.Field(
        'types.EmojiGroupPremium',
        alias='_'
    )

    title: str
    icon_emoji_id: int
