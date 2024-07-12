from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetFavedStickers(BaseModel):
    """
    functions.messages.GetFavedStickers
    ID: 0x4f1aaa9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetFavedStickers'] = pydantic.Field(
        'functions.messages.GetFavedStickers',
        alias='_'
    )

    hash: int
