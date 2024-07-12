from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleDialogPin(BaseModel):
    """
    functions.messages.ToggleDialogPin
    ID: 0xa731e257
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleDialogPin'] = pydantic.Field(
        'functions.messages.ToggleDialogPin',
        alias='_'
    )

    peer: "base.InputDialogPeer"
    pinned: typing.Optional[bool] = None
