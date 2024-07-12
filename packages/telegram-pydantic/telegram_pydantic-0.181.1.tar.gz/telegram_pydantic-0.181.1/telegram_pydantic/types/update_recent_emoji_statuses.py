from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateRecentEmojiStatuses(BaseModel):
    """
    types.UpdateRecentEmojiStatuses
    ID: 0x30f443db
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateRecentEmojiStatuses'] = pydantic.Field(
        'types.UpdateRecentEmojiStatuses',
        alias='_'
    )

