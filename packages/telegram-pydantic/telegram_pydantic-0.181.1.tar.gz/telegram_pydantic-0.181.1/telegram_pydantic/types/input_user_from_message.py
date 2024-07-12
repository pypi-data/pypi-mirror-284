from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUserFromMessage(BaseModel):
    """
    types.InputUserFromMessage
    ID: 0x1da448e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUserFromMessage'] = pydantic.Field(
        'types.InputUserFromMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    user_id: int
