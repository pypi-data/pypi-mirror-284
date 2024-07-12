from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportSpam(BaseModel):
    """
    functions.channels.ReportSpam
    ID: 0xf44a8315
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReportSpam'] = pydantic.Field(
        'functions.channels.ReportSpam',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
    id: list[int]
