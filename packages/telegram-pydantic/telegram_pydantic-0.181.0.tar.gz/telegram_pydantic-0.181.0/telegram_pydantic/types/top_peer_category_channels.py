from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryChannels(BaseModel):
    """
    types.TopPeerCategoryChannels
    ID: 0x161d9628
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryChannels'] = pydantic.Field(
        'types.TopPeerCategoryChannels',
        alias='_'
    )

