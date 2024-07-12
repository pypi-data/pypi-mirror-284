from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleUsername(BaseModel):
    """
    functions.channels.ToggleUsername
    ID: 0x50f24105
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleUsername'] = pydantic.Field(
        'functions.channels.ToggleUsername',
        alias='_'
    )

    channel: "base.InputChannel"
    username: str
    active: bool
