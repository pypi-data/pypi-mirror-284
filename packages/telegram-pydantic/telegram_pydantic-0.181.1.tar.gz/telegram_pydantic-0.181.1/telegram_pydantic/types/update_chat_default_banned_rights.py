from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateChatDefaultBannedRights(BaseModel):
    """
    types.UpdateChatDefaultBannedRights
    ID: 0x54c01850
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateChatDefaultBannedRights'] = pydantic.Field(
        'types.UpdateChatDefaultBannedRights',
        alias='_'
    )

    peer: "base.Peer"
    default_banned_rights: "base.ChatBannedRights"
    version: int
