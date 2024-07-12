from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryPhoneCalls(BaseModel):
    """
    types.TopPeerCategoryPhoneCalls
    ID: 0x1e76a78c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryPhoneCalls'] = pydantic.Field(
        'types.TopPeerCategoryPhoneCalls',
        alias='_'
    )

