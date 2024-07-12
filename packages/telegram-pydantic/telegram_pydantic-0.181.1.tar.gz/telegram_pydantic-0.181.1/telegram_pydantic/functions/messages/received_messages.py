from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedMessages(BaseModel):
    """
    functions.messages.ReceivedMessages
    ID: 0x5a954c0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReceivedMessages'] = pydantic.Field(
        'functions.messages.ReceivedMessages',
        alias='_'
    )

    max_id: int
