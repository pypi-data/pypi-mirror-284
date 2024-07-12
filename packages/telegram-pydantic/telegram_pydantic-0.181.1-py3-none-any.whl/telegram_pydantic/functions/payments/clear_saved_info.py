from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ClearSavedInfo(BaseModel):
    """
    functions.payments.ClearSavedInfo
    ID: 0xd83d70c1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.ClearSavedInfo'] = pydantic.Field(
        'functions.payments.ClearSavedInfo',
        alias='_'
    )

    credentials: typing.Optional[bool] = None
    info: typing.Optional[bool] = None
