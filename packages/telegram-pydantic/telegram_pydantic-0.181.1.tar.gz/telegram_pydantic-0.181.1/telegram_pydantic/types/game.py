from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Game(BaseModel):
    """
    types.Game
    ID: 0xbdf9653b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Game'] = pydantic.Field(
        'types.Game',
        alias='_'
    )

    id: int
    access_hash: int
    short_name: str
    title: str
    description: str
    photo: "base.Photo"
    document: typing.Optional["base.Document"] = None
