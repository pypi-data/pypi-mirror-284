from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebAuthorizations(BaseModel):
    """
    functions.account.GetWebAuthorizations
    ID: 0x182e6d6f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetWebAuthorizations'] = pydantic.Field(
        'functions.account.GetWebAuthorizations',
        alias='_'
    )

