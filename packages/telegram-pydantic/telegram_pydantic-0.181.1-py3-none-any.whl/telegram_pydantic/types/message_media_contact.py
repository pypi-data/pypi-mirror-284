from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaContact(BaseModel):
    """
    types.MessageMediaContact
    ID: 0x70322949
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaContact'] = pydantic.Field(
        'types.MessageMediaContact',
        alias='_'
    )

    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    user_id: int
