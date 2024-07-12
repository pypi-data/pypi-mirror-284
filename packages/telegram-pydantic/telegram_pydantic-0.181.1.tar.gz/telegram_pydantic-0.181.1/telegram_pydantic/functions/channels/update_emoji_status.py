from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEmojiStatus(BaseModel):
    """
    functions.channels.UpdateEmojiStatus
    ID: 0xf0d3e6a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.UpdateEmojiStatus'] = pydantic.Field(
        'functions.channels.UpdateEmojiStatus',
        alias='_'
    )

    channel: "base.InputChannel"
    emoji_status: "base.EmojiStatus"
