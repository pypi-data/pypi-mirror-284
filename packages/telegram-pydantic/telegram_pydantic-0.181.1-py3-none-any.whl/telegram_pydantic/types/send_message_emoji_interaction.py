from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageEmojiInteraction(BaseModel):
    """
    types.SendMessageEmojiInteraction
    ID: 0x25972bcb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageEmojiInteraction'] = pydantic.Field(
        'types.SendMessageEmojiInteraction',
        alias='_'
    )

    emoticon: str
    msg_id: int
    interaction: "base.DataJSON"
