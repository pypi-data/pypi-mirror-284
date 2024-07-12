from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolveBusinessChatLink(BaseModel):
    """
    functions.account.ResolveBusinessChatLink
    ID: 0x5492e5ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResolveBusinessChatLink'] = pydantic.Field(
        'functions.account.ResolveBusinessChatLink',
        alias='_'
    )

    slug: str
