from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsNotModified(BaseModel):
    """
    types.channels.ChannelParticipantsNotModified
    ID: 0xf0173fe9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.ChannelParticipantsNotModified'] = pydantic.Field(
        'types.channels.ChannelParticipantsNotModified',
        alias='_'
    )

