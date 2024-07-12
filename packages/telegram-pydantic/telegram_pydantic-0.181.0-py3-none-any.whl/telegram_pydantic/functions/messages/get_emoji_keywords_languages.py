from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetEmojiKeywordsLanguages(BaseModel):
    """
    functions.messages.GetEmojiKeywordsLanguages
    ID: 0x4e9963b2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetEmojiKeywordsLanguages'] = pydantic.Field(
        'functions.messages.GetEmojiKeywordsLanguages',
        alias='_'
    )

    lang_codes: list[str]
