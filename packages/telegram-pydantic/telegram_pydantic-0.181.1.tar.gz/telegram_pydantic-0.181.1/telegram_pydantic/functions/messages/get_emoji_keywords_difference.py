from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiKeywordsDifference(BaseModel):
    """
    functions.messages.GetEmojiKeywordsDifference
    ID: 0x1508b6af
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiKeywordsDifference'] = pydantic.Field(
        'functions.messages.GetEmojiKeywordsDifference',
        alias='_'
    )

    lang_code: str
    from_version: int
