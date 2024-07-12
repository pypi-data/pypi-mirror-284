from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportPeer(BaseModel):
    """
    functions.account.ReportPeer
    ID: 0xc5ba3d86
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ReportPeer'] = pydantic.Field(
        'functions.account.ReportPeer',
        alias='_'
    )

    peer: "base.InputPeer"
    reason: "base.ReportReason"
    message: str
