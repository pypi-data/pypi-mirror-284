from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportSpam(BaseModel):
    """
    functions.messages.ReportSpam
    ID: 0xcf1592db
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReportSpam'] = pydantic.Field(
        'functions.messages.ReportSpam',
        alias='_'
    )

    peer: "base.InputPeer"
