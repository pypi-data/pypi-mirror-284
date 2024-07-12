from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteBusinessChatLink(BaseModel):
    """
    functions.account.DeleteBusinessChatLink
    ID: 0x60073674
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteBusinessChatLink'] = pydantic.Field(
        'functions.account.DeleteBusinessChatLink',
        alias='_'
    )

    slug: str
