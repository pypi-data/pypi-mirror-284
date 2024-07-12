from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiKeywordsDifference(BaseModel):
    """
    types.EmojiKeywordsDifference
    ID: 0x5cc761bd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiKeywordsDifference'] = pydantic.Field(
        'types.EmojiKeywordsDifference',
        alias='_'
    )

    lang_code: str
    from_version: int
    version: int
    keywords: list["base.EmojiKeyword"]
