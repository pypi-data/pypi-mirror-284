from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportSponsoredMessage(BaseModel):
    """
    functions.channels.ReportSponsoredMessage
    ID: 0xaf8ff6b9
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReportSponsoredMessage'] = pydantic.Field(
        'functions.channels.ReportSponsoredMessage',
        alias='_'
    )

    channel: "base.InputChannel"
    random_id: bytes
    option: bytes
