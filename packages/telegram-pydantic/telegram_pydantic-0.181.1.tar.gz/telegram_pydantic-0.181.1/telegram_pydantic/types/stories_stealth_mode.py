from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class StoriesStealthMode(BaseModel):
    """
    types.StoriesStealthMode
    ID: 0x712e27fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.StoriesStealthMode'] = pydantic.Field(
        'types.StoriesStealthMode',
        alias='_'
    )

    active_until_date: typing.Optional[int] = None
    cooldown_until_date: typing.Optional[int] = None
