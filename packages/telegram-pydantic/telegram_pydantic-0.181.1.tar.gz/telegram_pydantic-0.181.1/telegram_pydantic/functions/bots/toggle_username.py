from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleUsername(BaseModel):
    """
    functions.bots.ToggleUsername
    ID: 0x53ca973
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.ToggleUsername'] = pydantic.Field(
        'functions.bots.ToggleUsername',
        alias='_'
    )

    bot: "base.InputUser"
    username: str
    active: bool
