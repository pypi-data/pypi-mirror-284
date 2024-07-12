from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResendPasswordEmail(BaseModel):
    """
    functions.account.ResendPasswordEmail
    ID: 0x7a7f2a15
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResendPasswordEmail'] = pydantic.Field(
        'functions.account.ResendPasswordEmail',
        alias='_'
    )

