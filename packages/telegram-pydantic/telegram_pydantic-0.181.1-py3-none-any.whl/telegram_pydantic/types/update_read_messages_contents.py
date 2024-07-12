from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateReadMessagesContents(BaseModel):
    """
    types.UpdateReadMessagesContents
    ID: 0xf8227181
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateReadMessagesContents'] = pydantic.Field(
        'types.UpdateReadMessagesContents',
        alias='_'
    )

    messages: list[int]
    pts: int
    pts_count: int
    date: typing.Optional[int] = None
