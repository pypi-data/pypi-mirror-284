from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClickSponsoredMessage(BaseModel):
    """
    functions.channels.ClickSponsoredMessage
    ID: 0x18afbc93
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ClickSponsoredMessage'] = pydantic.Field(
        'functions.channels.ClickSponsoredMessage',
        alias='_'
    )

    channel: "base.InputChannel"
    random_id: bytes
