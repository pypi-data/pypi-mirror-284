from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckUsername(BaseModel):
    """
    functions.channels.CheckUsername
    ID: 0x10e6bd2c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.CheckUsername'] = pydantic.Field(
        'functions.channels.CheckUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
