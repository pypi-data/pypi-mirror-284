from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBold(BaseModel):
    """
    types.MessageEntityBold
    ID: 0xbd610bc9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBold'] = pydantic.Field(
        'types.MessageEntityBold',
        alias='_'
    )

    offset: int
    length: int
