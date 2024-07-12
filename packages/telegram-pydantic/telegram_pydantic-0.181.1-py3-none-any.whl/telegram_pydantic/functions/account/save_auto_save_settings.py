from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAutoSaveSettings(BaseModel):
    """
    functions.account.SaveAutoSaveSettings
    ID: 0xd69b8361
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveAutoSaveSettings'] = pydantic.Field(
        'functions.account.SaveAutoSaveSettings',
        alias='_'
    )

    settings: "base.AutoSaveSettings"
    users: typing.Optional[bool] = None
    chats: typing.Optional[bool] = None
    broadcasts: typing.Optional[bool] = None
    peer: typing.Optional["base.InputPeer"] = None
