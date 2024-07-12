from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordInputSettings(BaseModel):
    """
    types.account.PasswordInputSettings
    ID: 0xc23727c9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.PasswordInputSettings'] = pydantic.Field(
        'types.account.PasswordInputSettings',
        alias='_'
    )

    new_algo: typing.Optional["base.PasswordKdfAlgo"] = None
    new_password_hash: typing.Optional[bytes] = None
    hint: typing.Optional[str] = None
    email: typing.Optional[str] = None
    new_secure_settings: typing.Optional["base.SecureSecretSettings"] = None
