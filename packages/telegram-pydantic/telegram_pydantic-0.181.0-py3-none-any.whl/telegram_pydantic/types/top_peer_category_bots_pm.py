from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryBotsPM(BaseModel):
    """
    types.TopPeerCategoryBotsPM
    ID: 0xab661b5b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryBotsPM'] = pydantic.Field(
        'types.TopPeerCategoryBotsPM',
        alias='_'
    )

