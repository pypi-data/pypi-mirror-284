from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LoginTokenSuccess(BaseModel):
    """
    types.auth.LoginTokenSuccess
    ID: 0x390d5c5e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.LoginTokenSuccess'] = pydantic.Field(
        'types.auth.LoginTokenSuccess',
        alias='_'
    )

    authorization: "base.auth.Authorization"
