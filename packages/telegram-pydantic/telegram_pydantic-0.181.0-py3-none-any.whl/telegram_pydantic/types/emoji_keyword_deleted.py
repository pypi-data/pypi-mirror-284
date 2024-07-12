from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeywordDeleted(BaseModel):
    """
    types.EmojiKeywordDeleted
    ID: 0x236df622
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeywordDeleted'] = pydantic.Field(
        'types.EmojiKeywordDeleted',
        alias='_'
    )

    keyword: str
    emoticons: list[str]
