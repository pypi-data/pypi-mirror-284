from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePendingJoinRequests(BaseModel):
    """
    types.UpdatePendingJoinRequests
    ID: 0x7063c3db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePendingJoinRequests'] = pydantic.Field(
        'types.UpdatePendingJoinRequests',
        alias='_'
    )

    peer: "base.Peer"
    requests_pending: int
    recent_requesters: list[int]
