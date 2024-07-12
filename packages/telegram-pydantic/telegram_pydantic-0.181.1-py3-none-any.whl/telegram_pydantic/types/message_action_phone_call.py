from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionPhoneCall(BaseModel):
    """
    types.MessageActionPhoneCall
    ID: 0x80e11a7f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionPhoneCall'] = pydantic.Field(
        'types.MessageActionPhoneCall',
        alias='_'
    )

    call_id: int
    video: typing.Optional[bool] = None
    reason: typing.Optional["base.PhoneCallDiscardReason"] = None
    duration: typing.Optional[int] = None
