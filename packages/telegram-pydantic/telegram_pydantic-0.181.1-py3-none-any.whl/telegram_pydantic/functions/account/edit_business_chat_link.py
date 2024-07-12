from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditBusinessChatLink(BaseModel):
    """
    functions.account.EditBusinessChatLink
    ID: 0x8c3410af
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.EditBusinessChatLink'] = pydantic.Field(
        'functions.account.EditBusinessChatLink',
        alias='_'
    )

    slug: str
    link: "base.InputBusinessChatLink"
