from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class QuickReply(BaseModel):
    """
    types.QuickReply
    ID: 0x697102b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.QuickReply'] = pydantic.Field(
        'types.QuickReply',
        alias='_'
    )

    shortcut_id: int
    shortcut: str
    top_message: int
    count: int
