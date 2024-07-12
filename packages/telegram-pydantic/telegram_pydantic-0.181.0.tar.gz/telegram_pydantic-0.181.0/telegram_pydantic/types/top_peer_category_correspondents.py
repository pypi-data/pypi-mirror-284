from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryCorrespondents(BaseModel):
    """
    types.TopPeerCategoryCorrespondents
    ID: 0x637b7ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryCorrespondents'] = pydantic.Field(
        'types.TopPeerCategoryCorrespondents',
        alias='_'
    )

