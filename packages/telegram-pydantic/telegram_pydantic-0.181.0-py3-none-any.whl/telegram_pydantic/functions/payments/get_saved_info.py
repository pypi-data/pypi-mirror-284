from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedInfo(BaseModel):
    """
    functions.payments.GetSavedInfo
    ID: 0x227d824b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.payments.GetSavedInfo'] = pydantic.Field(
        'functions.payments.GetSavedInfo',
        alias='_'
    )

