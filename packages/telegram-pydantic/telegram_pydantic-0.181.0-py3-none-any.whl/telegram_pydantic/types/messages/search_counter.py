from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SearchCounter(BaseModel):
    """
    types.messages.SearchCounter
    ID: 0xe844ebff
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SearchCounter'] = pydantic.Field(
        'types.messages.SearchCounter',
        alias='_'
    )

    filter: "base.MessagesFilter"
    count: int
    inexact: typing.Optional[bool] = None
