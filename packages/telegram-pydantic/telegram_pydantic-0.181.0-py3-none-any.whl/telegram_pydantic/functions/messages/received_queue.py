from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedQueue(BaseModel):
    """
    functions.messages.ReceivedQueue
    ID: 0x55a5bb66
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReceivedQueue'] = pydantic.Field(
        'functions.messages.ReceivedQueue',
        alias='_'
    )

    max_qts: int
