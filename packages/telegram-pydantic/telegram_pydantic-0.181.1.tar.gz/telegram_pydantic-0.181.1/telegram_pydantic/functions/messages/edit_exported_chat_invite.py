from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditExportedChatInvite(BaseModel):
    """
    functions.messages.EditExportedChatInvite
    ID: 0xbdca2f75
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditExportedChatInvite'] = pydantic.Field(
        'functions.messages.EditExportedChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    link: str
    revoked: typing.Optional[bool] = None
    expire_date: typing.Optional[int] = None
    usage_limit: typing.Optional[int] = None
    request_needed: typing.Optional[bool] = None
    title: typing.Optional[str] = None
