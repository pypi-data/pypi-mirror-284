from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetSecureValueErrors(BaseModel):
    """
    functions.users.SetSecureValueErrors
    ID: 0x90c894b5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.users.SetSecureValueErrors'] = pydantic.Field(
        'functions.users.SetSecureValueErrors',
        alias='_'
    )

    id: "base.InputUser"
    errors: list["base.SecureValueError"]
