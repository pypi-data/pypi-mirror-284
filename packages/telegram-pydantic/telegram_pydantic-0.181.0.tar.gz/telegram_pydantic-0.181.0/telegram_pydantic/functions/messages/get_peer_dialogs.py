from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPeerDialogs(BaseModel):
    """
    functions.messages.GetPeerDialogs
    ID: 0xe470bcfd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPeerDialogs'] = pydantic.Field(
        'functions.messages.GetPeerDialogs',
        alias='_'
    )

    peers: list["base.InputDialogPeer"]
