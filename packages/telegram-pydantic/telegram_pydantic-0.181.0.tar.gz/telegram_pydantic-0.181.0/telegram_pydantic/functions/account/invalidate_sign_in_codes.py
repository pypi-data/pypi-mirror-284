from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InvalidateSignInCodes(BaseModel):
    """
    functions.account.InvalidateSignInCodes
    ID: 0xca8ae8ba
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InvalidateSignInCodes'] = pydantic.Field(
        'functions.account.InvalidateSignInCodes',
        alias='_'
    )

    codes: list[str]
