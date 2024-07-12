from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessagesNotModified(BaseModel):
    """
    types.messages.MessagesNotModified
    ID: 0x74535f21
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.MessagesNotModified'] = pydantic.Field(
        'types.messages.MessagesNotModified',
        alias='_'
    )

    count: int
