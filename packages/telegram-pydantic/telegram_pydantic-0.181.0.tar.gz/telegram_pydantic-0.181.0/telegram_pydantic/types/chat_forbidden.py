from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChatForbidden(BaseModel):
    """
    types.ChatForbidden
    ID: 0x6592a1a7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChatForbidden'] = pydantic.Field(
        'types.ChatForbidden',
        alias='_'
    )

    id: int
    title: str
