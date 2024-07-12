from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportEncryptedSpam(BaseModel):
    """
    functions.messages.ReportEncryptedSpam
    ID: 0x4b0c8c0f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ReportEncryptedSpam'] = pydantic.Field(
        'functions.messages.ReportEncryptedSpam',
        alias='_'
    )

    peer: "base.InputEncryptedChat"
