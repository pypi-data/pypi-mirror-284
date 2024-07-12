from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatDefaultBannedRights(BaseModel):
    """
    functions.messages.EditChatDefaultBannedRights
    ID: 0xa5866b41
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatDefaultBannedRights'] = pydantic.Field(
        'functions.messages.EditChatDefaultBannedRights',
        alias='_'
    )

    peer: "base.InputPeer"
    banned_rights: "base.ChatBannedRights"
