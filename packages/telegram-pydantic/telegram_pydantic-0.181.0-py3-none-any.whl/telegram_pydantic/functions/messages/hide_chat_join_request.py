from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideChatJoinRequest(BaseModel):
    """
    functions.messages.HideChatJoinRequest
    ID: 0x7fe7e815
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HideChatJoinRequest'] = pydantic.Field(
        'functions.messages.HideChatJoinRequest',
        alias='_'
    )

    peer: "base.InputPeer"
    user_id: "base.InputUser"
    approved: typing.Optional[bool] = None
