from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerUserFromMessage(BaseModel):
    """
    types.InputPeerUserFromMessage
    ID: 0xa87b0a1c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerUserFromMessage'] = pydantic.Field(
        'types.InputPeerUserFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    user_id: int
