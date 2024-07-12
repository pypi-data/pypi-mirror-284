from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiGroups(BaseModel):
    """
    functions.messages.GetEmojiGroups
    ID: 0x7488ce5b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiGroups'] = pydantic.Field(
        'functions.messages.GetEmojiGroups',
        alias='_'
    )

    hash: int
