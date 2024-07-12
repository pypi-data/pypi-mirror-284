from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmailVerificationGoogle(BaseModel):
    """
    types.EmailVerificationGoogle
    ID: 0xdb909ec2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmailVerificationGoogle'] = pydantic.Field(
        'types.EmailVerificationGoogle',
        alias='_'
    )

    token: str
