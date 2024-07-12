from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionGroupCallScheduled(BaseModel):
    """
    types.MessageActionGroupCallScheduled
    ID: 0xb3a07661
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionGroupCallScheduled'] = pydantic.Field(
        'types.MessageActionGroupCallScheduled',
        alias='_'
    )

    call: "base.InputGroupCall"
    schedule_date: int
