from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteAutoSaveExceptions(BaseModel):
    """
    functions.account.DeleteAutoSaveExceptions
    ID: 0x53bc0020
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.DeleteAutoSaveExceptions'] = pydantic.Field(
        'functions.account.DeleteAutoSaveExceptions',
        alias='_'
    )

