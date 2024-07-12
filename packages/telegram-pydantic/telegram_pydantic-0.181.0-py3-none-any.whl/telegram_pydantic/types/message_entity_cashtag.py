from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityCashtag(BaseModel):
    """
    types.MessageEntityCashtag
    ID: 0x4c4e743f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityCashtag'] = pydantic.Field(
        'types.MessageEntityCashtag',
        alias='_'
    )

    offset: int
    length: int
