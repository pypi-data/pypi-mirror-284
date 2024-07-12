from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedPhoneContact(BaseModel):
    """
    types.SavedPhoneContact
    ID: 0x1142bd56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SavedPhoneContact'] = pydantic.Field(
        'types.SavedPhoneContact',
        alias='_'
    )

    phone: str
    first_name: str
    last_name: str
    date: int
