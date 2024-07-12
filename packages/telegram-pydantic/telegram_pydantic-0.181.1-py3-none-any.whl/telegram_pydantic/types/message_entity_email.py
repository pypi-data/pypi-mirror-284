from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityEmail(BaseModel):
    """
    types.MessageEntityEmail
    ID: 0x64e475c2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityEmail'] = pydantic.Field(
        'types.MessageEntityEmail',
        alias='_'
    )

    offset: int
    length: int
