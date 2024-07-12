from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGameScore(BaseModel):
    """
    types.MessageActionGameScore
    ID: 0x92a72876
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGameScore'] = pydantic.Field(
        'types.MessageActionGameScore',
        alias='_'
    )

    game_id: int
    score: int
