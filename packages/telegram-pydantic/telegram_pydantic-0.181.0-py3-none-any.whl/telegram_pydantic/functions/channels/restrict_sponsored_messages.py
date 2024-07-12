from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RestrictSponsoredMessages(BaseModel):
    """
    functions.channels.RestrictSponsoredMessages
    ID: 0x9ae91519
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.RestrictSponsoredMessages'] = pydantic.Field(
        'functions.channels.RestrictSponsoredMessages',
        alias='_'
    )

    channel: "base.InputChannel"
    restricted: bool
