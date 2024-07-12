from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockCover(BaseModel):
    """
    types.PageBlockCover
    ID: 0x39f23300
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockCover'] = pydantic.Field(
        'types.PageBlockCover',
        alias='_'
    )

    cover: "base.PageBlock"
