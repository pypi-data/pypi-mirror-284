from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerificationCode(BaseModel):
    """
    types.EmailVerificationCode
    ID: 0x922e55a9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerificationCode'] = pydantic.Field(
        'types.EmailVerificationCode',
        alias='_'
    )

    code: str
