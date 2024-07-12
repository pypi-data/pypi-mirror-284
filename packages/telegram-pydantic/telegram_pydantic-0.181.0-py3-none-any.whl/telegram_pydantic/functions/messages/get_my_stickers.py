from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMyStickers(BaseModel):
    """
    functions.messages.GetMyStickers
    ID: 0xd0b5e1fc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMyStickers'] = pydantic.Field(
        'functions.messages.GetMyStickers',
        alias='_'
    )

    offset_id: int
    limit: int
