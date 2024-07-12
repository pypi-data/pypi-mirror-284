from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChatInviteImporters(BaseModel):
    """
    functions.messages.GetChatInviteImporters
    ID: 0xdf04dd4e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetChatInviteImporters'] = pydantic.Field(
        'functions.messages.GetChatInviteImporters',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_date: int
    offset_user: "base.InputUser"
    limit: int
    requested: typing.Optional[bool] = None
    link: typing.Optional[str] = None
    q: typing.Optional[str] = None
