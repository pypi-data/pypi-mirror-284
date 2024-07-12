from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchGlobal(BaseModel):
    """
    functions.messages.SearchGlobal
    ID: 0x4bc6589a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchGlobal'] = pydantic.Field(
        'functions.messages.SearchGlobal',
        alias='_'
    )

    q: str
    filter: "base.MessagesFilter"
    min_date: int
    max_date: int
    offset_rate: int
    offset_peer: "base.InputPeer"
    offset_id: int
    limit: int
    broadcasts_only: typing.Optional[bool] = None
    folder_id: typing.Optional[int] = None
