from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelParticipantsMentions(BaseModel):
    """
    types.ChannelParticipantsMentions
    ID: 0xe04b5ceb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelParticipantsMentions'] = pydantic.Field(
        'types.ChannelParticipantsMentions',
        alias='_'
    )

    q: typing.Optional[str] = None
    top_msg_id: typing.Optional[int] = None
