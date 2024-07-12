from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearRecentStickers(BaseModel):
    """
    functions.messages.ClearRecentStickers
    ID: 0x8999602d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ClearRecentStickers'] = pydantic.Field(
        'functions.messages.ClearRecentStickers',
        alias='_'
    )

    attached: typing.Optional[bool] = None
