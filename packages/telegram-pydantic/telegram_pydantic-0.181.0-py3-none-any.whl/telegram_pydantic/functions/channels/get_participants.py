from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetParticipants(BaseModel):
    """
    functions.channels.GetParticipants
    ID: 0x77ced9d0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetParticipants'] = pydantic.Field(
        'functions.channels.GetParticipants',
        alias='_'
    )

    channel: "base.InputChannel"
    filter: "base.ChannelParticipantsFilter"
    offset: int
    limit: int
    hash: int
