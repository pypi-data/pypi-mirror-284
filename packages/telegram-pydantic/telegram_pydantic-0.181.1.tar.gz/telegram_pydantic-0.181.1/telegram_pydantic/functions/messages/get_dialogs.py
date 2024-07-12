from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDialogs(BaseModel):
    """
    functions.messages.GetDialogs
    ID: 0xa0f4cb4f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDialogs'] = pydantic.Field(
        'functions.messages.GetDialogs',
        alias='_'
    )

    offset_date: int
    offset_id: int
    offset_peer: "base.InputPeer"
    limit: int
    hash: int
    exclude_pinned: typing.Optional[bool] = None
    folder_id: typing.Optional[int] = None
