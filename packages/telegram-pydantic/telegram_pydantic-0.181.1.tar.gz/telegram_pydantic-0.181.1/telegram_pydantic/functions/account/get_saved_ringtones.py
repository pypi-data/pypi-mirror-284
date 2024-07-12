from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedRingtones(BaseModel):
    """
    functions.account.GetSavedRingtones
    ID: 0xe1902288
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetSavedRingtones'] = pydantic.Field(
        'functions.account.GetSavedRingtones',
        alias='_'
    )

    hash: int
