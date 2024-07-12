from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateUserEmojiStatus(BaseModel):
    """
    types.UpdateUserEmojiStatus
    ID: 0x28373599
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateUserEmojiStatus'] = pydantic.Field(
        'types.UpdateUserEmojiStatus',
        alias='_'
    )

    user_id: int
    emoji_status: "base.EmojiStatus"
