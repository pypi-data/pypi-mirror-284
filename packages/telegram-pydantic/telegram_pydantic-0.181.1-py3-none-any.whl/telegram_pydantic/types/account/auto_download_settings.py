from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoDownloadSettings(BaseModel):
    """
    types.account.AutoDownloadSettings
    ID: 0x63cacf26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.AutoDownloadSettings'] = pydantic.Field(
        'types.account.AutoDownloadSettings',
        alias='_'
    )

    low: "base.AutoDownloadSettings"
    medium: "base.AutoDownloadSettings"
    high: "base.AutoDownloadSettings"
