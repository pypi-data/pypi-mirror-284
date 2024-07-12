from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateEmojiStatus(BaseModel):
    """
    functions.account.UpdateEmojiStatus
    ID: 0xfbd3de6b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateEmojiStatus'] = pydantic.Field(
        'functions.account.UpdateEmojiStatus',
        alias='_'
    )

    emoji_status: "base.EmojiStatus"
