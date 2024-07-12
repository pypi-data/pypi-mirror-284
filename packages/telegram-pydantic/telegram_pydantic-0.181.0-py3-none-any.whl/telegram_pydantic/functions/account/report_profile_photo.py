from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportProfilePhoto(BaseModel):
    """
    functions.account.ReportProfilePhoto
    ID: 0xfa8cc6f5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ReportProfilePhoto'] = pydantic.Field(
        'functions.account.ReportProfilePhoto',
        alias='_'
    )

    peer: "base.InputPeer"
    photo_id: "base.InputPhoto"
    reason: "base.ReportReason"
    message: str
