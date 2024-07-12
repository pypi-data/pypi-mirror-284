from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageEntityBlockquote(BaseModel):
    """
    types.MessageEntityBlockquote
    ID: 0xf1ccaaac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageEntityBlockquote'] = pydantic.Field(
        'types.MessageEntityBlockquote',
        alias='_'
    )

    offset: int
    length: int
    collapsed: typing.Optional[bool] = None
