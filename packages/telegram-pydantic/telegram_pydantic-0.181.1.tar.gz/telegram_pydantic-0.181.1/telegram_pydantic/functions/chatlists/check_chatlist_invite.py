from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckChatlistInvite(BaseModel):
    """
    functions.chatlists.CheckChatlistInvite
    ID: 0x41c10fff
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.chatlists.CheckChatlistInvite'] = pydantic.Field(
        'functions.chatlists.CheckChatlistInvite',
        alias='_'
    )

    slug: str
