from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportChatInvite(BaseModel):
    """
    functions.messages.ExportChatInvite
    ID: 0xa02ce5d5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ExportChatInvite'] = pydantic.Field(
        'functions.messages.ExportChatInvite',
        alias='_'
    )

    peer: "base.InputPeer"
    legacy_revoke_permanent: typing.Optional[bool] = None
    request_needed: typing.Optional[bool] = None
    expire_date: typing.Optional[int] = None
    usage_limit: typing.Optional[int] = None
    title: typing.Optional[str] = None
