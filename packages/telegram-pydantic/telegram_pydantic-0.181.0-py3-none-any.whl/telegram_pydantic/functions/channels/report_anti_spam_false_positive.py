from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportAntiSpamFalsePositive(BaseModel):
    """
    functions.channels.ReportAntiSpamFalsePositive
    ID: 0xa850a693
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ReportAntiSpamFalsePositive'] = pydantic.Field(
        'functions.channels.ReportAntiSpamFalsePositive',
        alias='_'
    )

    channel: "base.InputChannel"
    msg_id: int
