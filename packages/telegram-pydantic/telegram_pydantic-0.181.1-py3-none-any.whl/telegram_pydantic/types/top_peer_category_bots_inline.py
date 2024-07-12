from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryBotsInline(BaseModel):
    """
    types.TopPeerCategoryBotsInline
    ID: 0x148677e2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryBotsInline'] = pydantic.Field(
        'types.TopPeerCategoryBotsInline',
        alias='_'
    )

