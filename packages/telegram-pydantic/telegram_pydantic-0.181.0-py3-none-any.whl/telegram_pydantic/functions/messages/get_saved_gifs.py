from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedGifs(BaseModel):
    """
    functions.messages.GetSavedGifs
    ID: 0x5cf09635
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSavedGifs'] = pydantic.Field(
        'functions.messages.GetSavedGifs',
        alias='_'
    )

    hash: int
