from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaContact(BaseModel):
    """
    types.InputMediaContact
    ID: 0xf8ab7dfb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaContact'] = pydantic.Field(
        'types.InputMediaContact',
        alias='_'
    )

    phone_number: str
    first_name: str
    last_name: str
    vcard: str
