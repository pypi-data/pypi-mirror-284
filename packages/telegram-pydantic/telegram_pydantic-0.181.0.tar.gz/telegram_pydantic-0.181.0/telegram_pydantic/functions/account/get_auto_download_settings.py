from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAutoDownloadSettings(BaseModel):
    """
    functions.account.GetAutoDownloadSettings
    ID: 0x56da0b3f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAutoDownloadSettings'] = pydantic.Field(
        'functions.account.GetAutoDownloadSettings',
        alias='_'
    )

