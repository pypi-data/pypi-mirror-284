from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStatuses(BaseModel):
    """
    functions.contacts.GetStatuses
    ID: 0xc4a353ee
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.GetStatuses'] = pydantic.Field(
        'functions.contacts.GetStatuses',
        alias='_'
    )

