from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiProfilePhotoGroups(BaseModel):
    """
    functions.messages.GetEmojiProfilePhotoGroups
    ID: 0x21a548f3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiProfilePhotoGroups'] = pydantic.Field(
        'functions.messages.GetEmojiProfilePhotoGroups',
        alias='_'
    )

    hash: int
