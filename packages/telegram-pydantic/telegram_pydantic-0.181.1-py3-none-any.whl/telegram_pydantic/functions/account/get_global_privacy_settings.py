from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGlobalPrivacySettings(BaseModel):
    """
    functions.account.GetGlobalPrivacySettings
    ID: 0xeb2b4cf6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetGlobalPrivacySettings'] = pydantic.Field(
        'functions.account.GetGlobalPrivacySettings',
        alias='_'
    )

