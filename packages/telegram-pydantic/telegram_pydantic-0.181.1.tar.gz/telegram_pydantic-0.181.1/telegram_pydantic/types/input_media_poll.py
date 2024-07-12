from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPoll(BaseModel):
    """
    types.InputMediaPoll
    ID: 0xf94e5f1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPoll'] = pydantic.Field(
        'types.InputMediaPoll',
        alias='_'
    )

    poll: "base.Poll"
    correct_answers: typing.Optional[list[bytes]] = None
    solution: typing.Optional[str] = None
    solution_entities: typing.Optional[list["base.MessageEntity"]] = None
