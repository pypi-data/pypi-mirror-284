from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPhoneContact(BaseModel):
    """
    types.InputPhoneContact
    ID: 0xf392b7f4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPhoneContact'] = pydantic.Field(
        'types.InputPhoneContact',
        alias='_'
    )

    client_id: int
    phone: str
    first_name: str
    last_name: str
