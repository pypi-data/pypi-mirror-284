from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetAutoSaveSettings(BaseModel):
    """
    functions.account.GetAutoSaveSettings
    ID: 0xadcbbcda
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetAutoSaveSettings'] = pydantic.Field(
        'functions.account.GetAutoSaveSettings',
        alias='_'
    )

