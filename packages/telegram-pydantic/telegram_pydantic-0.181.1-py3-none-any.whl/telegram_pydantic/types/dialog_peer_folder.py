from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogPeerFolder(BaseModel):
    """
    types.DialogPeerFolder
    ID: 0x514519e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogPeerFolder'] = pydantic.Field(
        'types.DialogPeerFolder',
        alias='_'
    )

    folder_id: int
