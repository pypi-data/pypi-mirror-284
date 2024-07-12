from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMaskStickers(BaseModel):
    """
    functions.messages.GetMaskStickers
    ID: 0x640f82b8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetMaskStickers'] = pydantic.Field(
        'functions.messages.GetMaskStickers',
        alias='_'
    )

    hash: int
