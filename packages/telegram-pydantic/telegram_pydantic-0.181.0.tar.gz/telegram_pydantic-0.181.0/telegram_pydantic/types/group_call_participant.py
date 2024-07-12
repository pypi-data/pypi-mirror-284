from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GroupCallParticipant(BaseModel):
    """
    types.GroupCallParticipant
    ID: 0xeba636fe
    Layer: 181
    """
    QUALNAME: typing.Literal['types.GroupCallParticipant'] = pydantic.Field(
        'types.GroupCallParticipant',
        alias='_'
    )

    peer: "base.Peer"
    date: int
    source: int
    muted: typing.Optional[bool] = None
    left: typing.Optional[bool] = None
    can_self_unmute: typing.Optional[bool] = None
    just_joined: typing.Optional[bool] = None
    versioned: typing.Optional[bool] = None
    min: typing.Optional[bool] = None
    muted_by_you: typing.Optional[bool] = None
    volume_by_admin: typing.Optional[bool] = None
    is_self: typing.Optional[bool] = pydantic.Field(None, alias='self')
    video_joined: typing.Optional[bool] = None
    active_date: typing.Optional[int] = None
    volume: typing.Optional[int] = None
    about: typing.Optional[str] = None
    raise_hand_rating: typing.Optional[int] = None
    video: typing.Optional["base.GroupCallParticipantVideo"] = None
    presentation: typing.Optional["base.GroupCallParticipantVideo"] = None
