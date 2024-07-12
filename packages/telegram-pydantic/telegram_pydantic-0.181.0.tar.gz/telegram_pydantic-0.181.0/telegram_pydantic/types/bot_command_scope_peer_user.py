from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopePeerUser(BaseModel):
    """
    types.BotCommandScopePeerUser
    ID: 0xa1321f3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopePeerUser'] = pydantic.Field(
        'types.BotCommandScopePeerUser',
        alias='_'
    )

    peer: "base.InputPeer"
    user_id: "base.InputUser"
