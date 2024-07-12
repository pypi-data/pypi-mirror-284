from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentStickers(BaseModel):
    """
    functions.messages.GetRecentStickers
    ID: 0x9da9403b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetRecentStickers'] = pydantic.Field(
        'functions.messages.GetRecentStickers',
        alias='_'
    )

    hash: int
    attached: typing.Optional[bool] = None
