from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AddContact(BaseModel):
    """
    functions.contacts.AddContact
    ID: 0xe8f463d0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.AddContact'] = pydantic.Field(
        'functions.contacts.AddContact',
        alias='_'
    )

    id: "base.InputUser"
    first_name: str
    last_name: str
    phone: str
    add_phone_privacy_exception: typing.Optional[bool] = None
