from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetContactIDs(BaseModel):
    """
    functions.contacts.GetContactIDs
    ID: 0x7adc669d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetContactIDs'] = pydantic.Field(
        'functions.contacts.GetContactIDs',
        alias='_'
    )

    hash: int
