from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FinishTakeoutSession(BaseModel):
    """
    functions.account.FinishTakeoutSession
    ID: 0x1d2652ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.FinishTakeoutSession'] = pydantic.Field(
        'functions.account.FinishTakeoutSession',
        alias='_'
    )

    success: typing.Optional[bool] = None
