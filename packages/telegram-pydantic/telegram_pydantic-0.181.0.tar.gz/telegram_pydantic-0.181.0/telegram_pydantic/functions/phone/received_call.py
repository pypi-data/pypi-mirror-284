from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReceivedCall(BaseModel):
    """
    functions.phone.ReceivedCall
    ID: 0x17d54f61
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ReceivedCall'] = pydantic.Field(
        'functions.phone.ReceivedCall',
        alias='_'
    )

    peer: "base.InputPhoneCall"
