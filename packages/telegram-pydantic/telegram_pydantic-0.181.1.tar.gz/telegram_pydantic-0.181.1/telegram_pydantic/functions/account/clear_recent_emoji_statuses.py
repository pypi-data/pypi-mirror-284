from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearRecentEmojiStatuses(BaseModel):
    """
    functions.account.ClearRecentEmojiStatuses
    ID: 0x18201aae
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ClearRecentEmojiStatuses'] = pydantic.Field(
        'functions.account.ClearRecentEmojiStatuses',
        alias='_'
    )

