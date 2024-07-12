from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotBroadcastDefaultAdminRights(BaseModel):
    """
    functions.bots.SetBotBroadcastDefaultAdminRights
    ID: 0x788464e1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotBroadcastDefaultAdminRights'] = pydantic.Field(
        'functions.bots.SetBotBroadcastDefaultAdminRights',
        alias='_'
    )

    admin_rights: "base.ChatAdminRights"
