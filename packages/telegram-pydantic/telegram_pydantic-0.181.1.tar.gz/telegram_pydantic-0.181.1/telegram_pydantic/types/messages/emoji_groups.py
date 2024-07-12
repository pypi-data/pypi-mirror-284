from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroups(BaseModel):
    """
    types.messages.EmojiGroups
    ID: 0x881fb94b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.EmojiGroups'] = pydantic.Field(
        'types.messages.EmojiGroups',
        alias='_'
    )

    hash: int
    groups: list["base.EmojiGroup"]
