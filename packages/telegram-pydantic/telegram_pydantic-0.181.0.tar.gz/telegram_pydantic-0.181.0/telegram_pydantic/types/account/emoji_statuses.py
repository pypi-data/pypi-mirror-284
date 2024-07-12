from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EmojiStatuses(BaseModel):
    """
    types.account.EmojiStatuses
    ID: 0x90c467d1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.EmojiStatuses'] = pydantic.Field(
        'types.account.EmojiStatuses',
        alias='_'
    )

    hash: int
    statuses: list["base.EmojiStatus"]
