from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockList(BaseModel):
    """
    types.PageBlockList
    ID: 0xe4e88011
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockList'] = pydantic.Field(
        'types.PageBlockList',
        alias='_'
    )

    items: list["base.PageListItem"]
