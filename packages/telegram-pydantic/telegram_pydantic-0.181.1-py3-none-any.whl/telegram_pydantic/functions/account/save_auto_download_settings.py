from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAutoDownloadSettings(BaseModel):
    """
    functions.account.SaveAutoDownloadSettings
    ID: 0x76f36233
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveAutoDownloadSettings'] = pydantic.Field(
        'functions.account.SaveAutoDownloadSettings',
        alias='_'
    )

    settings: "base.AutoDownloadSettings"
    low: typing.Optional[bool] = None
    high: typing.Optional[bool] = None
