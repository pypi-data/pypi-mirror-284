from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedGifs(BaseModel):
    """
    types.messages.SavedGifs
    ID: 0x84a02a0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SavedGifs'] = pydantic.Field(
        'types.messages.SavedGifs',
        alias='_'
    )

    hash: int
    gifs: list["base.Document"]
