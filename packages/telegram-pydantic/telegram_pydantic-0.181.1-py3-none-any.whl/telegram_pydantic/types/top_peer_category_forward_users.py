from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryForwardUsers(BaseModel):
    """
    types.TopPeerCategoryForwardUsers
    ID: 0xa8406ca9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryForwardUsers'] = pydantic.Field(
        'types.TopPeerCategoryForwardUsers',
        alias='_'
    )

