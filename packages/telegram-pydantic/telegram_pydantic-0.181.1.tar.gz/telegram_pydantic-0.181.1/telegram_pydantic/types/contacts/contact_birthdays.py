from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactBirthdays(BaseModel):
    """
    types.contacts.ContactBirthdays
    ID: 0x114ff30d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.contacts.ContactBirthdays'] = pydantic.Field(
        'types.contacts.ContactBirthdays',
        alias='_'
    )

    contacts: list["base.ContactBirthday"]
    users: list["base.User"]
