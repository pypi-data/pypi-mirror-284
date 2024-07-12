from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePhoneCallSignalingData(BaseModel):
    """
    types.UpdatePhoneCallSignalingData
    ID: 0x2661bf09
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePhoneCallSignalingData'] = pydantic.Field(
        'types.UpdatePhoneCallSignalingData',
        alias='_'
    )

    phone_call_id: int
    data: bytes
