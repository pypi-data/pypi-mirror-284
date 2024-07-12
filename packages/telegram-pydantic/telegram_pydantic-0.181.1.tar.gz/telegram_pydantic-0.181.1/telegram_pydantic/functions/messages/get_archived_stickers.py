from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetArchivedStickers(BaseModel):
    """
    functions.messages.GetArchivedStickers
    ID: 0x57f17692
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetArchivedStickers'] = pydantic.Field(
        'functions.messages.GetArchivedStickers',
        alias='_'
    )

    offset_id: int
    limit: int
    masks: typing.Optional[bool] = None
    emojis: typing.Optional[bool] = None
