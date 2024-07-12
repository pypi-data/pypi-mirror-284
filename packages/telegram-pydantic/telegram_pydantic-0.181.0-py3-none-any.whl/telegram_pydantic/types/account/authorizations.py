from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Authorizations(BaseModel):
    """
    types.account.Authorizations
    ID: 0x4bff8ea0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Authorizations'] = pydantic.Field(
        'types.account.Authorizations',
        alias='_'
    )

    authorization_ttl_days: int
    authorizations: list["base.Authorization"]
