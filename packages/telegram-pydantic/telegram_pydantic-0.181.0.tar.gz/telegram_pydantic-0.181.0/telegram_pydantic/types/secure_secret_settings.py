from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SecureSecretSettings(BaseModel):
    """
    types.SecureSecretSettings
    ID: 0x1527bcac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SecureSecretSettings'] = pydantic.Field(
        'types.SecureSecretSettings',
        alias='_'
    )

    secure_algo: "base.SecurePasswordKdfAlgo"
    secure_secret: bytes
    secure_secret_id: int
