from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DiscardCall(BaseModel):
    """
    functions.phone.DiscardCall
    ID: 0xb2cbc1c0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.DiscardCall'] = pydantic.Field(
        'functions.phone.DiscardCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    duration: int
    reason: "base.PhoneCallDiscardReason"
    connection_id: int
    video: typing.Optional[bool] = None
