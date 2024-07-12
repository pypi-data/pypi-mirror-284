from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetGlobalPrivacySettings(BaseModel):
    """
    functions.account.SetGlobalPrivacySettings
    ID: 0x1edaaac2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetGlobalPrivacySettings'] = pydantic.Field(
        'functions.account.SetGlobalPrivacySettings',
        alias='_'
    )

    settings: "base.GlobalPrivacySettings"
