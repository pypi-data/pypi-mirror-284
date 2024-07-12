from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerifyPurposeLoginSetup(BaseModel):
    """
    types.EmailVerifyPurposeLoginSetup
    ID: 0x4345be73
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerifyPurposeLoginSetup'] = pydantic.Field(
        'types.EmailVerifyPurposeLoginSetup',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
