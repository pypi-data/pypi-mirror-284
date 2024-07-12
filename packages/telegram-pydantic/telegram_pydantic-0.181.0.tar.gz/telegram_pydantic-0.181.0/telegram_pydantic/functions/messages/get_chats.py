from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChats(BaseModel):
    """
    functions.messages.GetChats
    ID: 0x49e9528f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetChats'] = pydantic.Field(
        'functions.messages.GetChats',
        alias='_'
    )

    id: list[int]
