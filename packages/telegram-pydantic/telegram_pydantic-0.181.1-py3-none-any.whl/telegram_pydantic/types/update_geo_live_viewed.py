from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateGeoLiveViewed(BaseModel):
    """
    types.UpdateGeoLiveViewed
    ID: 0x871fb939
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateGeoLiveViewed'] = pydantic.Field(
        'types.UpdateGeoLiveViewed',
        alias='_'
    )

    peer: "base.Peer"
    msg_id: int
