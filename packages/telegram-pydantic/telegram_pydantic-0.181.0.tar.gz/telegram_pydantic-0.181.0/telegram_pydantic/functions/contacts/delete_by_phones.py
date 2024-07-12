from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeleteByPhones(BaseModel):
    """
    functions.contacts.DeleteByPhones
    ID: 0x1013fd9e
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.DeleteByPhones'] = pydantic.Field(
        'functions.contacts.DeleteByPhones',
        alias='_'
    )

    phones: list[str]
