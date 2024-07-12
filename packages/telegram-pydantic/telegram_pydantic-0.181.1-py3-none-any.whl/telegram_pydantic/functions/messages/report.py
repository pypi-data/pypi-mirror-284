from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Report(BaseModel):
    """
    functions.messages.Report
    ID: 0x8953ab4e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.Report'] = pydantic.Field(
        'functions.messages.Report',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
    reason: "base.ReportReason"
    message: str
