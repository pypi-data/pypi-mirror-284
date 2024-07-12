from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGameHighScores(BaseModel):
    """
    functions.messages.GetGameHighScores
    ID: 0xe822649d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetGameHighScores'] = pydantic.Field(
        'functions.messages.GetGameHighScores',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    user_id: "base.InputUser"
