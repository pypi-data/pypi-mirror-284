from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockAnchor(BaseModel):
    """
    types.PageBlockAnchor
    ID: 0xce0d37b0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockAnchor'] = pydantic.Field(
        'types.PageBlockAnchor',
        alias='_'
    )

    name: str
