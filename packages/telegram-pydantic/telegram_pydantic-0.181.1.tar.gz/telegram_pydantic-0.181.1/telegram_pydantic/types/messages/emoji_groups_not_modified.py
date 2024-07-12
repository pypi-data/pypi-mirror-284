from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiGroupsNotModified(BaseModel):
    """
    types.messages.EmojiGroupsNotModified
    ID: 0x6fb4ad87
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.EmojiGroupsNotModified'] = pydantic.Field(
        'types.messages.EmojiGroupsNotModified',
        alias='_'
    )

