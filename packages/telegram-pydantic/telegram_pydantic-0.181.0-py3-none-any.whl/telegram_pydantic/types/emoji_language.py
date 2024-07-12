from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiLanguage(BaseModel):
    """
    types.EmojiLanguage
    ID: 0xb3fb5361
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiLanguage'] = pydantic.Field(
        'types.EmojiLanguage',
        alias='_'
    )

    lang_code: str
