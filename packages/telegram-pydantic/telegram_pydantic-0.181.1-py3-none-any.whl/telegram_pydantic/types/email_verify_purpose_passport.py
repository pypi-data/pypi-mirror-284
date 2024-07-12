from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerifyPurposePassport(BaseModel):
    """
    types.EmailVerifyPurposePassport
    ID: 0xbbf51685
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerifyPurposePassport'] = pydantic.Field(
        'types.EmailVerifyPurposePassport',
        alias='_'
    )

