from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetBirthdays(BaseModel):
    """
    functions.contacts.GetBirthdays
    ID: 0xdaeda864
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetBirthdays'] = pydantic.Field(
        'functions.contacts.GetBirthdays',
        alias='_'
    )

