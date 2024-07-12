from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebAuthorizations(BaseModel):
    """
    types.account.WebAuthorizations
    ID: 0xed56c9fc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.WebAuthorizations'] = pydantic.Field(
        'types.account.WebAuthorizations',
        alias='_'
    )

    authorizations: list["base.WebAuthorization"]
    users: list["base.User"]
