from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HideAllChatJoinRequests(BaseModel):
    """
    functions.messages.HideAllChatJoinRequests
    ID: 0xe085f4ea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HideAllChatJoinRequests'] = pydantic.Field(
        'functions.messages.HideAllChatJoinRequests',
        alias='_'
    )

    peer: "base.InputPeer"
    approved: typing.Optional[bool] = None
    link: typing.Optional[str] = None
