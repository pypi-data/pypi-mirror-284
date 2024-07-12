from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetReactionsNotifySettings(BaseModel):
    """
    functions.account.SetReactionsNotifySettings
    ID: 0x316ce548
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetReactionsNotifySettings'] = pydantic.Field(
        'functions.account.SetReactionsNotifySettings',
        alias='_'
    )

    settings: "base.ReactionsNotifySettings"
