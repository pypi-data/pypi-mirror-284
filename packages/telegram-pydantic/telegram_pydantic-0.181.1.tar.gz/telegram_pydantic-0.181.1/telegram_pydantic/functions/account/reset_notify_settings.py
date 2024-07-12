from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetNotifySettings(BaseModel):
    """
    functions.account.ResetNotifySettings
    ID: 0xdb7e1747
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetNotifySettings'] = pydantic.Field(
        'functions.account.ResetNotifySettings',
        alias='_'
    )

