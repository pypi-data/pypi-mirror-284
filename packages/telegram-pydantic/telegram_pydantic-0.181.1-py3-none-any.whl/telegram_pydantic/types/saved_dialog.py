from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedDialog(BaseModel):
    """
    types.SavedDialog
    ID: 0xbd87cb6c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SavedDialog'] = pydantic.Field(
        'types.SavedDialog',
        alias='_'
    )

    peer: "base.Peer"
    top_message: int
    pinned: typing.Optional[bool] = None
