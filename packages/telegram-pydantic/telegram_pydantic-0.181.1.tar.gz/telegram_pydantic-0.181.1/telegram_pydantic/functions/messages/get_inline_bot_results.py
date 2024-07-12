from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInlineBotResults(BaseModel):
    """
    functions.messages.GetInlineBotResults
    ID: 0x514e999d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetInlineBotResults'] = pydantic.Field(
        'functions.messages.GetInlineBotResults',
        alias='_'
    )

    bot: "base.InputUser"
    peer: "base.InputPeer"
    query: str
    offset: str
    geo_point: typing.Optional["base.InputGeoPoint"] = None
