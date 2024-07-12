from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiList(BaseModel):
    """
    types.EmojiList
    ID: 0x7a1e11d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiList'] = pydantic.Field(
        'types.EmojiList',
        alias='_'
    )

    hash: int
    document_id: list[int]
