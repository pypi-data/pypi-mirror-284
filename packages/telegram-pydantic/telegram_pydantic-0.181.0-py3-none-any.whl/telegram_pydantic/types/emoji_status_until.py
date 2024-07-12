from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatusUntil(BaseModel):
    """
    types.EmojiStatusUntil
    ID: 0xfa30a8c7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiStatusUntil'] = pydantic.Field(
        'types.EmojiStatusUntil',
        alias='_'
    )

    document_id: int
    until: int
