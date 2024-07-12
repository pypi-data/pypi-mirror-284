from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelDefaultEmojiStatuses(BaseModel):
    """
    functions.account.GetChannelDefaultEmojiStatuses
    ID: 0x7727a7d5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetChannelDefaultEmojiStatuses'] = pydantic.Field(
        'functions.account.GetChannelDefaultEmojiStatuses',
        alias='_'
    )

    hash: int
