from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveCallLog(BaseModel):
    """
    functions.phone.SaveCallLog
    ID: 0x41248786
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SaveCallLog'] = pydantic.Field(
        'functions.phone.SaveCallLog',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    file: "base.InputFile"
