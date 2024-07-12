from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleParticipantsHidden(BaseModel):
    """
    functions.channels.ToggleParticipantsHidden
    ID: 0x6a6e7854
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleParticipantsHidden'] = pydantic.Field(
        'functions.channels.ToggleParticipantsHidden',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
