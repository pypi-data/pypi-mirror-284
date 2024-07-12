from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BotCommandScopePeer(BaseModel):
    """
    types.BotCommandScopePeer
    ID: 0xdb9d897d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.BotCommandScopePeer'] = pydantic.Field(
        'types.BotCommandScopePeer',
        alias='_'
    )

    peer: "base.InputPeer"
