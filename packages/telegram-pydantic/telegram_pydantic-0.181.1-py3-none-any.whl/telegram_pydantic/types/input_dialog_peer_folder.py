from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDialogPeerFolder(BaseModel):
    """
    types.InputDialogPeerFolder
    ID: 0x64600527
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDialogPeerFolder'] = pydantic.Field(
        'types.InputDialogPeerFolder',
        alias='_'
    )

    folder_id: int
