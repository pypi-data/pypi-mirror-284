from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchSentMedia(BaseModel):
    """
    functions.messages.SearchSentMedia
    ID: 0x107e31a0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SearchSentMedia'] = pydantic.Field(
        'functions.messages.SearchSentMedia',
        alias='_'
    )

    q: str
    filter: "base.MessagesFilter"
    limit: int
