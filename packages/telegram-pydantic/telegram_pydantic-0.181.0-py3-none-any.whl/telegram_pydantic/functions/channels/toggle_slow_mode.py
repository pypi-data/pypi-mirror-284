from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSlowMode(BaseModel):
    """
    functions.channels.ToggleSlowMode
    ID: 0xedd49ef0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleSlowMode'] = pydantic.Field(
        'functions.channels.ToggleSlowMode',
        alias='_'
    )

    channel: "base.InputChannel"
    seconds: int
