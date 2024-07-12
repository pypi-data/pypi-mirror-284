from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageListOrderedItemBlocks(BaseModel):
    """
    types.PageListOrderedItemBlocks
    ID: 0x98dd8936
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageListOrderedItemBlocks'] = pydantic.Field(
        'types.PageListOrderedItemBlocks',
        alias='_'
    )

    num: str
    blocks: list["base.PageBlock"]
