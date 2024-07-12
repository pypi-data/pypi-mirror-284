from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetExportedInvites(BaseModel):
    """
    functions.chatlists.GetExportedInvites
    ID: 0xce03da83
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.GetExportedInvites'] = pydantic.Field(
        'functions.chatlists.GetExportedInvites',
        alias='_'
    )

    chatlist: "base.InputChatlist"
