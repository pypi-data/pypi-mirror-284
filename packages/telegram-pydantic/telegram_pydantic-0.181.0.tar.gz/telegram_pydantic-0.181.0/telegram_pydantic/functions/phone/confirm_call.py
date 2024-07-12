from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConfirmCall(BaseModel):
    """
    functions.phone.ConfirmCall
    ID: 0x2efe1722
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ConfirmCall'] = pydantic.Field(
        'functions.phone.ConfirmCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    g_a: bytes
    key_fingerprint: int
    protocol: "base.PhoneCallProtocol"
