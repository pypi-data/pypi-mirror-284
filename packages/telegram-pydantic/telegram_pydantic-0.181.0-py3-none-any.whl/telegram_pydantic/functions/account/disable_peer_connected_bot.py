from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DisablePeerConnectedBot(BaseModel):
    """
    functions.account.DisablePeerConnectedBot
    ID: 0x5e437ed9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DisablePeerConnectedBot'] = pydantic.Field(
        'functions.account.DisablePeerConnectedBot',
        alias='_'
    )

    peer: "base.InputPeer"
