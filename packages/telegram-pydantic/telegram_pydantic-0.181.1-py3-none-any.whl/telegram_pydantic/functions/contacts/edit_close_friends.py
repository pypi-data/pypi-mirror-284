from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditCloseFriends(BaseModel):
    """
    functions.contacts.EditCloseFriends
    ID: 0xba6705f0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.EditCloseFriends'] = pydantic.Field(
        'functions.contacts.EditCloseFriends',
        alias='_'
    )

    id: list[int]
