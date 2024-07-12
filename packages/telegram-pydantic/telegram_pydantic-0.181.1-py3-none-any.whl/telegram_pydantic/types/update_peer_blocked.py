from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePeerBlocked(BaseModel):
    """
    types.UpdatePeerBlocked
    ID: 0xebe07752
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePeerBlocked'] = pydantic.Field(
        'types.UpdatePeerBlocked',
        alias='_'
    )

    peer_id: "base.Peer"
    blocked: typing.Optional[bool] = None
    blocked_my_stories_from: typing.Optional[bool] = None
