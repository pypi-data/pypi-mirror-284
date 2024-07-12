from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PhoneCall(BaseModel):
    """
    types.PhoneCall
    ID: 0x30535af5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PhoneCall'] = pydantic.Field(
        'types.PhoneCall',
        alias='_'
    )

    id: int
    access_hash: int
    date: int
    admin_id: int
    participant_id: int
    g_a_or_b: bytes
    key_fingerprint: int
    protocol: "base.PhoneCallProtocol"
    connections: list["base.PhoneConnection"]
    start_date: int
    p2p_allowed: typing.Optional[bool] = None
    video: typing.Optional[bool] = None
    custom_parameters: typing.Optional["base.DataJSON"] = None
