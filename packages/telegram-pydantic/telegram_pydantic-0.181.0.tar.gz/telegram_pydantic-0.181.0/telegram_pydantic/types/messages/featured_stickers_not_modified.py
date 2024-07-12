from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FeaturedStickersNotModified(BaseModel):
    """
    types.messages.FeaturedStickersNotModified
    ID: 0xc6dc0c66
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.FeaturedStickersNotModified'] = pydantic.Field(
        'types.messages.FeaturedStickersNotModified',
        alias='_'
    )

    count: int
