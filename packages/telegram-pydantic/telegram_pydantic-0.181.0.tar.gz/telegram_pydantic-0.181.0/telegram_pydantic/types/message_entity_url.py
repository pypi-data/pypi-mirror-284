from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityUrl(BaseModel):
    """
    types.MessageEntityUrl
    ID: 0x6ed02538
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityUrl'] = pydantic.Field(
        'types.MessageEntityUrl',
        alias='_'
    )

    offset: int
    length: int
