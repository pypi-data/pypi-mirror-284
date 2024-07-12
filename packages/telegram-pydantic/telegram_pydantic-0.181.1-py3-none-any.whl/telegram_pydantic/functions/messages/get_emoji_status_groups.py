from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiStatusGroups(BaseModel):
    """
    functions.messages.GetEmojiStatusGroups
    ID: 0x2ecd56cd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiStatusGroups'] = pydantic.Field(
        'functions.messages.GetEmojiStatusGroups',
        alias='_'
    )

    hash: int
