from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultEmojiStatuses(BaseModel):
    """
    functions.account.GetDefaultEmojiStatuses
    ID: 0xd6753386
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultEmojiStatuses'] = pydantic.Field(
        'functions.account.GetDefaultEmojiStatuses',
        alias='_'
    )

    hash: int
