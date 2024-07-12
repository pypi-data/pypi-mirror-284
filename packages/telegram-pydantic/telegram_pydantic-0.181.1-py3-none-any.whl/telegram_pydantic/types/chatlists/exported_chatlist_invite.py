from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedChatlistInvite(BaseModel):
    """
    types.chatlists.ExportedChatlistInvite
    ID: 0x10e6e3a6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.chatlists.ExportedChatlistInvite'] = pydantic.Field(
        'types.chatlists.ExportedChatlistInvite',
        alias='_'
    )

    filter: "base.DialogFilter"
    invite: "base.ExportedChatlistInvite"
