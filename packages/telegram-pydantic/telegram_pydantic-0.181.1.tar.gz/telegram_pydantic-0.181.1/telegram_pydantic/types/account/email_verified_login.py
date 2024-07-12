from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerifiedLogin(BaseModel):
    """
    types.account.EmailVerifiedLogin
    ID: 0xe1bb0d61
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmailVerifiedLogin'] = pydantic.Field(
        'types.account.EmailVerifiedLogin',
        alias='_'
    )

    email: str
    sent_code: "base.auth.SentCode"
