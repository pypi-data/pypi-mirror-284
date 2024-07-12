from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Search(BaseModel):
    """
    functions.contacts.Search
    ID: 0x11f812d8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.Search'] = pydantic.Field(
        'functions.contacts.Search',
        alias='_'
    )

    q: str
    limit: int
