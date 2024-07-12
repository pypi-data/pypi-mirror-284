from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Poll(BaseModel):
    """
    types.Poll
    ID: 0x58747131
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Poll'] = pydantic.Field(
        'types.Poll',
        alias='_'
    )

    id: int
    question: "base.TextWithEntities"
    answers: list["base.PollAnswer"]
    closed: typing.Optional[bool] = None
    public_voters: typing.Optional[bool] = None
    multiple_choice: typing.Optional[bool] = None
    quiz: typing.Optional[bool] = None
    close_period: typing.Optional[int] = None
    close_date: typing.Optional[int] = None
