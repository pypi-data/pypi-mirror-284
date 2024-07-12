from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatusesNotModified(BaseModel):
    """
    types.account.EmojiStatusesNotModified
    ID: 0xd08ce645
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmojiStatusesNotModified'] = pydantic.Field(
        'types.account.EmojiStatusesNotModified',
        alias='_'
    )

