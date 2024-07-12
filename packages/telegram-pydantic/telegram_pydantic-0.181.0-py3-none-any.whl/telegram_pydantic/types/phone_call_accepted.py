from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCallAccepted(BaseModel):
    """
    types.PhoneCallAccepted
    ID: 0x3660c311
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCallAccepted'] = pydantic.Field(
        'types.PhoneCallAccepted',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
    g_b: bytes
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
