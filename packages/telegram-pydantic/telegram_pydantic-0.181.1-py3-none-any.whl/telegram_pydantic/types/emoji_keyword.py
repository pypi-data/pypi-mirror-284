from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeyword(BaseModel):
    """
    types.EmojiKeyword
    ID: 0xd5b3b9f9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeyword'] = pydantic.Field(
        'types.EmojiKeyword',
        alias='_'
    )

    keyword: str
    emoticons: list[str]
