from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptCall(BaseModel):
    """
    functions.phone.AcceptCall
    ID: 0x3bd2b4a0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.AcceptCall'] = pydantic.Field(
        'functions.phone.AcceptCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    g_b: bytes
    protocol: "base.PhoneCallProtocol"
