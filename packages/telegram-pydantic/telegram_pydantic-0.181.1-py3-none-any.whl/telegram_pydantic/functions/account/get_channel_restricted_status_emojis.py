from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetChannelRestrictedStatusEmojis(BaseModel):
    """
    functions.account.GetChannelRestrictedStatusEmojis
    ID: 0x35a9e0d5
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetChannelRestrictedStatusEmojis'] = pydantic.Field(
        'functions.account.GetChannelRestrictedStatusEmojis',
        alias='_'
    )

    hash: int
