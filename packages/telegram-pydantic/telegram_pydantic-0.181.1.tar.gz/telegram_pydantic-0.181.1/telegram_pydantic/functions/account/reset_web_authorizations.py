from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetWebAuthorizations(BaseModel):
    """
    functions.account.ResetWebAuthorizations
    ID: 0x682d2594
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetWebAuthorizations'] = pydantic.Field(
        'functions.account.ResetWebAuthorizations',
        alias='_'
    )

