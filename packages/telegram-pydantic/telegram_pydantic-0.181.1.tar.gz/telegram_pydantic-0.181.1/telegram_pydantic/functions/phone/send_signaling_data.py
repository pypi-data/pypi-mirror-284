from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendSignalingData(BaseModel):
    """
    functions.phone.SendSignalingData
    ID: 0xff7a9383
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SendSignalingData'] = pydantic.Field(
        'functions.phone.SendSignalingData',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    data: bytes
