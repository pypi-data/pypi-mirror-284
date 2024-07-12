from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionCustomEmoji(BaseModel):
    """
    types.ReactionCustomEmoji
    ID: 0x8935fc73
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionCustomEmoji'] = pydantic.Field(
        'types.ReactionCustomEmoji',
        alias='_'
    )

    document_id: int
