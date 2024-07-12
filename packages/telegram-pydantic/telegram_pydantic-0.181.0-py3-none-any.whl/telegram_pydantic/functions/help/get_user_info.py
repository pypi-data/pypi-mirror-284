from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetUserInfo(BaseModel):
    """
    functions.help.GetUserInfo
    ID: 0x38a08d3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetUserInfo'] = pydantic.Field(
        'functions.help.GetUserInfo',
        alias='_'
    )

    user_id: "base.InputUser"
