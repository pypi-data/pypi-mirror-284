from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RecoverPassword(BaseModel):
    """
    functions.auth.RecoverPassword
    ID: 0x37096c70
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.RecoverPassword'] = pydantic.Field(
        'functions.auth.RecoverPassword',
        alias='_'
    )

    code: str
    new_settings: typing.Optional["base.account.PasswordInputSettings"] = None
