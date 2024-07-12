from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryForwardChats(BaseModel):
    """
    types.TopPeerCategoryForwardChats
    ID: 0xfbeec0f0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryForwardChats'] = pydantic.Field(
        'types.TopPeerCategoryForwardChats',
        alias='_'
    )

