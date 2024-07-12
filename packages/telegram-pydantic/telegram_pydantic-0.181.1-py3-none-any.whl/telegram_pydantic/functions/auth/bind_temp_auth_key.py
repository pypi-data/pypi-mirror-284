from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class BindTempAuthKey(BaseModel):
    """
    functions.auth.BindTempAuthKey
    ID: 0xcdd42a05
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.BindTempAuthKey'] = pydantic.Field(
        'functions.auth.BindTempAuthKey',
        alias='_'
    )

    perm_auth_key_id: int
    nonce: int
    expires_at: int
    encrypted_message: bytes
