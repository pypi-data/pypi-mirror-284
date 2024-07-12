from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultGroupPhotoEmojis(BaseModel):
    """
    functions.account.GetDefaultGroupPhotoEmojis
    ID: 0x915860ae
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultGroupPhotoEmojis'] = pydantic.Field(
        'functions.account.GetDefaultGroupPhotoEmojis',
        alias='_'
    )

    hash: int
