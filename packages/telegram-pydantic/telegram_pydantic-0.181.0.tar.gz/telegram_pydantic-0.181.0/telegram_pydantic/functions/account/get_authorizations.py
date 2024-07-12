from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAuthorizations(BaseModel):
    """
    functions.account.GetAuthorizations
    ID: 0xe320c158
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAuthorizations'] = pydantic.Field(
        'functions.account.GetAuthorizations',
        alias='_'
    )

