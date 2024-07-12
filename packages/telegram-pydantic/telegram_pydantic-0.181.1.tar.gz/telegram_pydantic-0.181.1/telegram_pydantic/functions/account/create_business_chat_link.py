from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateBusinessChatLink(BaseModel):
    """
    functions.account.CreateBusinessChatLink
    ID: 0x8851e68e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CreateBusinessChatLink'] = pydantic.Field(
        'functions.account.CreateBusinessChatLink',
        alias='_'
    )

    link: "base.InputBusinessChatLink"
