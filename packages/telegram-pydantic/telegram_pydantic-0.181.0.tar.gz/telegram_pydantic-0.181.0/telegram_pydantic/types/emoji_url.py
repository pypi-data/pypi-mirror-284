from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiURL(BaseModel):
    """
    types.EmojiURL
    ID: 0xa575739d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiURL'] = pydantic.Field(
        'types.EmojiURL',
        alias='_'
    )

    url: str
