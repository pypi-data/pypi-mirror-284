from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBusinessChatLinks(BaseModel):
    """
    functions.account.GetBusinessChatLinks
    ID: 0x6f70dde1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetBusinessChatLinks'] = pydantic.Field(
        'functions.account.GetBusinessChatLinks',
        alias='_'
    )

