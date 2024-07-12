from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CancelPasswordEmail(BaseModel):
    """
    functions.account.CancelPasswordEmail
    ID: 0xc1cbd5b6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CancelPasswordEmail'] = pydantic.Field(
        'functions.account.CancelPasswordEmail',
        alias='_'
    )

