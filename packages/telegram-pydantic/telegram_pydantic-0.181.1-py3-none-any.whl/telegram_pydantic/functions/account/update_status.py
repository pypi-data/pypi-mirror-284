from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateStatus(BaseModel):
    """
    functions.account.UpdateStatus
    ID: 0x6628562c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateStatus'] = pydantic.Field(
        'functions.account.UpdateStatus',
        alias='_'
    )

    offline: bool
