from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ViewSponsoredMessage(BaseModel):
    """
    functions.channels.ViewSponsoredMessage
    ID: 0xbeaedb94
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ViewSponsoredMessage'] = pydantic.Field(
        'functions.channels.ViewSponsoredMessage',
        alias='_'
    )

    channel: "base.InputChannel"
    random_id: bytes
