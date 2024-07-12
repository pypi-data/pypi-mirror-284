from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PollAnswerVoters(BaseModel):
    """
    types.PollAnswerVoters
    ID: 0x3b6ddad2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PollAnswerVoters'] = pydantic.Field(
        'types.PollAnswerVoters',
        alias='_'
    )

    option: bytes
    voters: int
    chosen: typing.Optional[bool] = None
    correct: typing.Optional[bool] = None
