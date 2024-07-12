from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetConnectedBots(BaseModel):
    """
    functions.account.GetConnectedBots
    ID: 0x4ea4c80f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetConnectedBots'] = pydantic.Field(
        'functions.account.GetConnectedBots',
        alias='_'
    )

