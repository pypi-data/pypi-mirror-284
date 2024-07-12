from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Password(BaseModel):
    """
    types.account.Password
    ID: 0x957b50fb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Password'] = pydantic.Field(
        'types.account.Password',
        alias='_'
    )

    new_algo: "base.PasswordKdfAlgo"
    new_secure_algo: "base.SecurePasswordKdfAlgo"
    secure_random: bytes
    has_recovery: typing.Optional[bool] = None
    has_secure_values: typing.Optional[bool] = None
    has_password: typing.Optional[bool] = None
    current_algo: typing.Optional["base.PasswordKdfAlgo"] = None
    srp_B: typing.Optional[bytes] = None
    srp_id: typing.Optional[int] = None
    hint: typing.Optional[str] = None
    email_unconfirmed_pattern: typing.Optional[str] = None
    pending_reset_date: typing.Optional[int] = None
    login_email_pattern: typing.Optional[str] = None
