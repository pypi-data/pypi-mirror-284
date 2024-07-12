from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HighScores(BaseModel):
    """
    types.messages.HighScores
    ID: 0x9a3bfd99
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.HighScores'] = pydantic.Field(
        'types.messages.HighScores',
        alias='_'
    )

    scores: list["base.HighScore"]
    users: list["base.User"]
