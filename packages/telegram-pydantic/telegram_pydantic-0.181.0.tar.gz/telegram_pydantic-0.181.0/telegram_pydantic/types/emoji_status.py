from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatus(BaseModel):
    """
    types.EmojiStatus
    ID: 0x929b619d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.EmojiStatus'] = pydantic.Field(
        'types.EmojiStatus',
        alias='_'
    )

    document_id: int
