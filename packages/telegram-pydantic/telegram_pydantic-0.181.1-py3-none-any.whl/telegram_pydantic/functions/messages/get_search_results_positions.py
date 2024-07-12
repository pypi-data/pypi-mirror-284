from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSearchResultsPositions(BaseModel):
    """
    functions.messages.GetSearchResultsPositions
    ID: 0x9c7f2f10
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSearchResultsPositions'] = pydantic.Field(
        'functions.messages.GetSearchResultsPositions',
        alias='_'
    )

    peer: "base.InputPeer"
    filter: "base.MessagesFilter"
    offset_id: int
    limit: int
    saved_peer_id: typing.Optional["base.InputPeer"] = None
