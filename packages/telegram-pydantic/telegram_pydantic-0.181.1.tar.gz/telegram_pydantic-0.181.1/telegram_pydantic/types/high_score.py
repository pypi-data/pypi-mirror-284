from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HighScore(BaseModel):
    """
    types.HighScore
    ID: 0x73a379eb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.HighScore'] = pydantic.Field(
        'types.HighScore',
        alias='_'
    )

    pos: int
    user_id: int
    score: int
