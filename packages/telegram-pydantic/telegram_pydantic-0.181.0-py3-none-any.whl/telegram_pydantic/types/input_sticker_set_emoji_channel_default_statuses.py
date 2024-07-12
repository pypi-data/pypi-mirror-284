from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickerSetEmojiChannelDefaultStatuses(BaseModel):
    """
    types.InputStickerSetEmojiChannelDefaultStatuses
    ID: 0x49748553
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickerSetEmojiChannelDefaultStatuses'] = pydantic.Field(
        'types.InputStickerSetEmojiChannelDefaultStatuses',
        alias='_'
    )

