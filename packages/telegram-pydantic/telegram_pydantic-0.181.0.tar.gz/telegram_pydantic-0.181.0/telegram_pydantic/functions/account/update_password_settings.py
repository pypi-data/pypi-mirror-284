from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePasswordSettings(BaseModel):
    """
    functions.account.UpdatePasswordSettings
    ID: 0xa59b102f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdatePasswordSettings'] = pydantic.Field(
        'functions.account.UpdatePasswordSettings',
        alias='_'
    )

    password: "base.InputCheckPasswordSRP"
    new_settings: "base.account.PasswordInputSettings"
