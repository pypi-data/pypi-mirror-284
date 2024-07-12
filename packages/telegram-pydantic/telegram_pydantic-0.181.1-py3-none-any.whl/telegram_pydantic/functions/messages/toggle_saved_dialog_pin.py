from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSavedDialogPin(BaseModel):
    """
    functions.messages.ToggleSavedDialogPin
    ID: 0xac81bbde
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleSavedDialogPin'] = pydantic.Field(
        'functions.messages.ToggleSavedDialogPin',
        alias='_'
    )

    peer: "base.InputDialogPeer"
    pinned: typing.Optional[bool] = None
