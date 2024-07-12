from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UnregisterDevice(BaseModel):
    """
    functions.account.UnregisterDevice
    ID: 0x6a0d3206
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UnregisterDevice'] = pydantic.Field(
        'functions.account.UnregisterDevice',
        alias='_'
    )

    token_type: int
    token: str
    other_uids: list[int]
