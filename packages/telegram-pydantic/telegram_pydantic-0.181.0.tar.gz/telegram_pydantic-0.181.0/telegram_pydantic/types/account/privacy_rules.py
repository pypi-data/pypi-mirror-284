from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyRules(BaseModel):
    """
    types.account.PrivacyRules
    ID: 0x50a04e45
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.PrivacyRules'] = pydantic.Field(
        'types.account.PrivacyRules',
        alias='_'
    )

    rules: list["base.PrivacyRule"]
    chats: list["base.Chat"]
    users: list["base.User"]
