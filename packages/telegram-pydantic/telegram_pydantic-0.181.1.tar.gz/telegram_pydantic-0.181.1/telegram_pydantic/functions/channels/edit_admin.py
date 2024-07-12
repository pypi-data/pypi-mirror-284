from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditAdmin(BaseModel):
    """
    functions.channels.EditAdmin
    ID: 0xd33c8902
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditAdmin'] = pydantic.Field(
        'functions.channels.EditAdmin',
        alias='_'
    )

    channel: "base.InputChannel"
    user_id: "base.InputUser"
    admin_rights: "base.ChatAdminRights"
    rank: str
