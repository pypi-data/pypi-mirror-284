from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentLocations(BaseModel):
    """
    functions.messages.GetRecentLocations
    ID: 0x702a40e0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetRecentLocations'] = pydantic.Field(
        'functions.messages.GetRecentLocations',
        alias='_'
    )

    peer: "base.InputPeer"
    limit: int
    hash: int
