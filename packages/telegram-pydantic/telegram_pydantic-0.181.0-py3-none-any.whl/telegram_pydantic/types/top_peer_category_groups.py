from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryGroups(BaseModel):
    """
    types.TopPeerCategoryGroups
    ID: 0xbd17a14a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryGroups'] = pydantic.Field(
        'types.TopPeerCategoryGroups',
        alias='_'
    )

