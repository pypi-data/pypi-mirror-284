from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallWaiting(BaseModel):
    """
    types.PhoneCallWaiting
    ID: 0xc5226f17
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallWaiting'] = pydantic.Field(
        'types.PhoneCallWaiting',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
    receive_date: typing.Optional[int] = None
