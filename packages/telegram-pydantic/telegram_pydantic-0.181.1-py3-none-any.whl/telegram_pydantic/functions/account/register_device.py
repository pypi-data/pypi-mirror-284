from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class RegisterDevice(BaseModel):
    """
    functions.account.RegisterDevice
    ID: 0xec86017a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.RegisterDevice'] = pydantic.Field(
        'functions.account.RegisterDevice',
        alias='_'
    )

    token_type: int
    token: str
    app_sandbox: bool
    secret: bytes
    other_uids: list[int]
    no_muted: typing.Optional[bool] = None
