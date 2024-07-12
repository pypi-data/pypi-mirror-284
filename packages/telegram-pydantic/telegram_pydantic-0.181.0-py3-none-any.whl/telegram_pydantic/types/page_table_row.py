from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageTableRow(BaseModel):
    """
    types.PageTableRow
    ID: 0xe0c0c5e5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageTableRow'] = pydantic.Field(
        'types.PageTableRow',
        alias='_'
    )

    cells: list["base.PageTableCell"]
