from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedDialogPinned(BaseModel):
    """
    types.UpdateSavedDialogPinned
    ID: 0xaeaf9e74
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateSavedDialogPinned'] = pydantic.Field(
        'types.UpdateSavedDialogPinned',
        alias='_'
    )

    peer: "base.DialogPeer"
    pinned: typing.Optional[bool] = None
