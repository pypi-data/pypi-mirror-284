from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContactBirthday(BaseModel):
    """
    types.ContactBirthday
    ID: 0x1d998733
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ContactBirthday'] = pydantic.Field(
        'types.ContactBirthday',
        alias='_'
    )

    contact_id: int
    birthday: "base.Birthday"
