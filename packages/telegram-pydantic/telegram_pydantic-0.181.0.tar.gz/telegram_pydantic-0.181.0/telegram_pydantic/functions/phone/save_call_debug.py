from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveCallDebug(BaseModel):
    """
    functions.phone.SaveCallDebug
    ID: 0x277add7e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SaveCallDebug'] = pydantic.Field(
        'functions.phone.SaveCallDebug',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    debug: "base.DataJSON"
