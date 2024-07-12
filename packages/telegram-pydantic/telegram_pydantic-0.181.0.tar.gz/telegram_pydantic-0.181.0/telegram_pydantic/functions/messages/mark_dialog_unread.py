from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MarkDialogUnread(BaseModel):
    """
    functions.messages.MarkDialogUnread
    ID: 0xc286d98f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.MarkDialogUnread'] = pydantic.Field(
        'functions.messages.MarkDialogUnread',
        alias='_'
    )

    peer: "base.InputDialogPeer"
    unread: typing.Optional[bool] = None
