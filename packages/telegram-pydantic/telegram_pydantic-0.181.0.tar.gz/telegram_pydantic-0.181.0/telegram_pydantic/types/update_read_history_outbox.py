from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadHistoryOutbox(BaseModel):
    """
    types.UpdateReadHistoryOutbox
    ID: 0x2f2f21bf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadHistoryOutbox'] = pydantic.Field(
        'types.UpdateReadHistoryOutbox',
        alias='_'
    )

    peer: "base.Peer"
    max_id: int
    pts: int
    pts_count: int
