from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleUsername(BaseModel):
    """
    functions.account.ToggleUsername
    ID: 0x58d6b376
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ToggleUsername'] = pydantic.Field(
        'functions.account.ToggleUsername',
        alias='_'
    )

    username: str
    active: bool
