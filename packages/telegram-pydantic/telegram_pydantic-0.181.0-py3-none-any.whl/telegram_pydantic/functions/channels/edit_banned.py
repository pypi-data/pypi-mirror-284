from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditBanned(BaseModel):
    """
    functions.channels.EditBanned
    ID: 0x96e6cd81
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditBanned'] = pydantic.Field(
        'functions.channels.EditBanned',
        alias='_'
    )

    channel: "base.InputChannel"
    participant: "base.InputPeer"
    banned_rights: "base.ChatBannedRights"
