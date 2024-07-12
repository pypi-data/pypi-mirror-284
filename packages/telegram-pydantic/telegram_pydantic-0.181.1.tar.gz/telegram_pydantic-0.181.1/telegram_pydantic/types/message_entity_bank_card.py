from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBankCard(BaseModel):
    """
    types.MessageEntityBankCard
    ID: 0x761e6af4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBankCard'] = pydantic.Field(
        'types.MessageEntityBankCard',
        alias='_'
    )

    offset: int
    length: int
