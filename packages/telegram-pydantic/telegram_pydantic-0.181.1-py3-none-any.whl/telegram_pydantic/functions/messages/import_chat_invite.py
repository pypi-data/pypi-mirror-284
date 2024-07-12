from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ImportChatInvite(BaseModel):
    """
    functions.messages.ImportChatInvite
    ID: 0x6c50051c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ImportChatInvite'] = pydantic.Field(
        'functions.messages.ImportChatInvite',
        alias='_'
    )

    hash: str
