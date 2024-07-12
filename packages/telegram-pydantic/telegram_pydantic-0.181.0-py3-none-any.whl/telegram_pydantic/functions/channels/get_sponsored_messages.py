from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSponsoredMessages(BaseModel):
    """
    functions.channels.GetSponsoredMessages
    ID: 0xec210fbf
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetSponsoredMessages'] = pydantic.Field(
        'functions.channels.GetSponsoredMessages',
        alias='_'
    )

    channel: "base.InputChannel"
