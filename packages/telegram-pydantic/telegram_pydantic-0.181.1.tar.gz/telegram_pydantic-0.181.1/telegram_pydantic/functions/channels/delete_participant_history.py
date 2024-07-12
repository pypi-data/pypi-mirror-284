from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteParticipantHistory(BaseModel):
    """
    functions.channels.DeleteParticipantHistory
    ID: 0x367544db
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeleteParticipantHistory'] = pydantic.Field(
        'functions.channels.DeleteParticipantHistory',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
