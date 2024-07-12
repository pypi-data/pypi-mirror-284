from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PasswordSettings(BaseModel):
    """
    types.account.PasswordSettings
    ID: 0x9a5c33e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.PasswordSettings'] = pydantic.Field(
        'types.account.PasswordSettings',
        alias='_'
    )

    email: typing.Optional[str] = None
    secure_settings: typing.Optional["base.SecureSecretSettings"] = None
