from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDefaultProfilePhotoEmojis(BaseModel):
    """
    functions.account.GetDefaultProfilePhotoEmojis
    ID: 0xe2750328
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetDefaultProfilePhotoEmojis'] = pydantic.Field(
        'functions.account.GetDefaultProfilePhotoEmojis',
        alias='_'
    )

    hash: int
