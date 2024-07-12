from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAllStickers(BaseModel):
    """
    functions.messages.GetAllStickers
    ID: 0xb8a0a1a8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetAllStickers'] = pydantic.Field(
        'functions.messages.GetAllStickers',
        alias='_'
    )

    hash: int
