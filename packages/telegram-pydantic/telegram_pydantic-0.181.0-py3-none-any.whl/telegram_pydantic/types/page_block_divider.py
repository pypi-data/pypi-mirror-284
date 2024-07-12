from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockDivider(BaseModel):
    """
    types.PageBlockDivider
    ID: 0xdb20b188
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockDivider'] = pydantic.Field(
        'types.PageBlockDivider',
        alias='_'
    )

