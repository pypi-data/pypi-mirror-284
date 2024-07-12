from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSearchResultsCalendar(BaseModel):
    """
    functions.messages.GetSearchResultsCalendar
    ID: 0x6aa3f6bd
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSearchResultsCalendar'] = pydantic.Field(
        'functions.messages.GetSearchResultsCalendar',
        alias='_'
    )

    peer: "base.InputPeer"
    filter: "base.MessagesFilter"
    offset_id: int
    offset_date: int
    saved_peer_id: typing.Optional["base.InputPeer"] = None
