from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedHistory(BaseModel):
    """
    functions.messages.GetSavedHistory
    ID: 0x3d9a414d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSavedHistory'] = pydantic.Field(
        'functions.messages.GetSavedHistory',
        alias='_'
    )

    peer: "base.InputPeer"
    offset_id: int
    offset_date: int
    add_offset: int
    limit: int
    max_id: int
    min_id: int
    hash: int
