from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatOnlines(BaseModel):
    """
    types.ChatOnlines
    ID: 0xf041e250
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatOnlines'] = pydantic.Field(
        'types.ChatOnlines',
        alias='_'
    )

    onlines: int
