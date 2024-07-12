from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelRecommendations(BaseModel):
    """
    functions.channels.GetChannelRecommendations
    ID: 0x25a71742
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetChannelRecommendations'] = pydantic.Field(
        'functions.channels.GetChannelRecommendations',
        alias='_'
    )

    channel: typing.Optional["base.InputChannel"] = None
