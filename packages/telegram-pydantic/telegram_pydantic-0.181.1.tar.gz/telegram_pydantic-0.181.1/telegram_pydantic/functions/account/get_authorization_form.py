from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAuthorizationForm(BaseModel):
    """
    functions.account.GetAuthorizationForm
    ID: 0xa929597a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAuthorizationForm'] = pydantic.Field(
        'functions.account.GetAuthorizationForm',
        alias='_'
    )

    bot_id: int
    scope: str
    public_key: str
