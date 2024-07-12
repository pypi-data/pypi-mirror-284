from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolvePhone(BaseModel):
    """
    functions.contacts.ResolvePhone
    ID: 0x8af94344
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ResolvePhone'] = pydantic.Field(
        'functions.contacts.ResolvePhone',
        alias='_'
    )

    phone: str
