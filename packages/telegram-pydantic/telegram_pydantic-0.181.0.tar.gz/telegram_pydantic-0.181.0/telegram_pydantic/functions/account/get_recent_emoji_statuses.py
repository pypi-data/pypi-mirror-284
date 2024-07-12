from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentEmojiStatuses(BaseModel):
    """
    functions.account.GetRecentEmojiStatuses
    ID: 0xf578105
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetRecentEmojiStatuses'] = pydantic.Field(
        'functions.account.GetRecentEmojiStatuses',
        alias='_'
    )

    hash: int
