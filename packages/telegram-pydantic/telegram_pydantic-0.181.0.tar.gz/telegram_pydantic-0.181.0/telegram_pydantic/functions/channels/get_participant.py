from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetParticipant(BaseModel):
    """
    functions.channels.GetParticipant
    ID: 0xa0ab6cc6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetParticipant'] = pydantic.Field(
        'functions.channels.GetParticipant',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
