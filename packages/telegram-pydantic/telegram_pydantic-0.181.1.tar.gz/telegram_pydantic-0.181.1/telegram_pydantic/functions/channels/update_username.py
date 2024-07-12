from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUsername(BaseModel):
    """
    functions.channels.UpdateUsername
    ID: 0x3514b3de
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.UpdateUsername'] = pydantic.Field(
        'functions.channels.UpdateUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
