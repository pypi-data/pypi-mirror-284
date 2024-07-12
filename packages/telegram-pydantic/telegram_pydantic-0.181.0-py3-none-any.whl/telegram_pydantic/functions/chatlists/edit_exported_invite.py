from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditExportedInvite(BaseModel):
    """
    functions.chatlists.EditExportedInvite
    ID: 0x653db63d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.EditExportedInvite'] = pydantic.Field(
        'functions.chatlists.EditExportedInvite',
        alias='_'
    )

    chatlist: "base.InputChatlist"
    slug: str
    title: typing.Optional[str] = None
    peers: typing.Optional[list["base.InputPeer"]] = None
