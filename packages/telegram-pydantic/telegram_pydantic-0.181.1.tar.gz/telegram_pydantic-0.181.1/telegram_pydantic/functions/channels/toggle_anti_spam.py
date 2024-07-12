from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleAntiSpam(BaseModel):
    """
    functions.channels.ToggleAntiSpam
    ID: 0x68f3e4eb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleAntiSpam'] = pydantic.Field(
        'functions.channels.ToggleAntiSpam',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
