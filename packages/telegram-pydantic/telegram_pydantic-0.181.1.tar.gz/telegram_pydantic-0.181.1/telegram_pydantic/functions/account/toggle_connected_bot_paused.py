from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleConnectedBotPaused(BaseModel):
    """
    functions.account.ToggleConnectedBotPaused
    ID: 0x646e1097
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ToggleConnectedBotPaused'] = pydantic.Field(
        'functions.account.ToggleConnectedBotPaused',
        alias='_'
    )

    peer: "base.InputPeer"
    paused: bool
