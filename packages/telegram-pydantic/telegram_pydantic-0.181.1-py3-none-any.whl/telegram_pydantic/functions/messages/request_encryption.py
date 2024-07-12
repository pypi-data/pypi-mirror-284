from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RequestEncryption(BaseModel):
    """
    functions.messages.RequestEncryption
    ID: 0xf64daf43
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.RequestEncryption'] = pydantic.Field(
        'functions.messages.RequestEncryption',
        alias='_'
    )

    user_id: "base.InputUser"
    random_id: int
    g_a: bytes
