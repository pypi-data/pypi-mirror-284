from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatusEmpty(BaseModel):
    """
    types.EmojiStatusEmpty
    ID: 0x2de11aae
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiStatusEmpty'] = pydantic.Field(
        'types.EmojiStatusEmpty',
        alias='_'
    )

