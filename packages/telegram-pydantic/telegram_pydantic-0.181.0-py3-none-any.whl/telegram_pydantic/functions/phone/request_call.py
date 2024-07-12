from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestCall(BaseModel):
    """
    functions.phone.RequestCall
    ID: 0x42ff96ed
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.RequestCall'] = pydantic.Field(
        'functions.phone.RequestCall',
        alias='_'
    )

    user_id: "base.InputUser"
    random_id: int
    g_a_hash: bytes
    protocol: "base.PhoneCallProtocol"
    video: typing.Optional[bool] = None
