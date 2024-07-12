from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiListNotModified(BaseModel):
    """
    types.EmojiListNotModified
    ID: 0x481eadfa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiListNotModified'] = pydantic.Field(
        'types.EmojiListNotModified',
        alias='_'
    )

