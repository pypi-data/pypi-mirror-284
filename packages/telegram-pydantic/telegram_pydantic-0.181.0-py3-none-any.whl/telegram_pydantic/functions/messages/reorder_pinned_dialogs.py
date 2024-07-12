from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReorderPinnedDialogs(BaseModel):
    """
    functions.messages.ReorderPinnedDialogs
    ID: 0x3b1adf37
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReorderPinnedDialogs'] = pydantic.Field(
        'functions.messages.ReorderPinnedDialogs',
        alias='_'
    )

    folder_id: int
    order: list["base.InputDialogPeer"]
    force: typing.Optional[bool] = None
