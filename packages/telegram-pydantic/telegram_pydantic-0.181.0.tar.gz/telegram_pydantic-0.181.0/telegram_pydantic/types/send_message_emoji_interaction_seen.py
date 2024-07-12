from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageEmojiInteractionSeen(BaseModel):
    """
    types.SendMessageEmojiInteractionSeen
    ID: 0xb665902e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageEmojiInteractionSeen'] = pydantic.Field(
        'types.SendMessageEmojiInteractionSeen',
        alias='_'
    )

    emoticon: str
