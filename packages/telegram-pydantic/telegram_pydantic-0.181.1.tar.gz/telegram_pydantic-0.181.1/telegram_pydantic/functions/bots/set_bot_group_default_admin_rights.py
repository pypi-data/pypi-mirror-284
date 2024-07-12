from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBotGroupDefaultAdminRights(BaseModel):
    """
    functions.bots.SetBotGroupDefaultAdminRights
    ID: 0x925ec9ea
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.bots.SetBotGroupDefaultAdminRights'] = pydantic.Field(
        'functions.bots.SetBotGroupDefaultAdminRights',
        alias='_'
    )

    admin_rights: "base.ChatAdminRights"
