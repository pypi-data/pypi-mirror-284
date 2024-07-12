from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoSaveSettings(BaseModel):
    """
    types.account.AutoSaveSettings
    ID: 0x4c3e069d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.AutoSaveSettings'] = pydantic.Field(
        'types.account.AutoSaveSettings',
        alias='_'
    )

    users_settings: "base.AutoSaveSettings"
    chats_settings: "base.AutoSaveSettings"
    broadcasts_settings: "base.AutoSaveSettings"
    exceptions: list["base.AutoSaveException"]
    chats: list["base.Chat"]
    users: list["base.User"]
