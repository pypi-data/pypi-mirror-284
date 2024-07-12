from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Contact(BaseModel):
    """
    types.Contact
    ID: 0x145ade0b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Contact'] = pydantic.Field(
        'types.Contact',
        alias='_'
    )

    user_id: int
    mutual: bool
