from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityCode(BaseModel):
    """
    types.MessageEntityCode
    ID: 0x28a20571
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityCode'] = pydantic.Field(
        'types.MessageEntityCode',
        alias='_'
    )

    offset: int
    length: int
