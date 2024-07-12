from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockTable(BaseModel):
    """
    types.PageBlockTable
    ID: 0xbf4dea82
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockTable'] = pydantic.Field(
        'types.PageBlockTable',
        alias='_'
    )

    title: "base.RichText"
    rows: list["base.PageTableRow"]
    bordered: typing.Optional[bool] = None
    striped: typing.Optional[bool] = None
