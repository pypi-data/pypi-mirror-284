from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListItemBlocks(BaseModel):
    """
    types.PageListItemBlocks
    ID: 0x25e073fc
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListItemBlocks'] = pydantic.Field(
        'types.PageListItemBlocks',
        alias='_'
    )

    blocks: list["base.PageBlock"]
