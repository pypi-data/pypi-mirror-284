from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetReactionsNotifySettings(BaseModel):
    """
    functions.account.GetReactionsNotifySettings
    ID: 0x6dd654c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetReactionsNotifySettings'] = pydantic.Field(
        'functions.account.GetReactionsNotifySettings',
        alias='_'
    )

