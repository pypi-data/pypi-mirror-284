from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockCollage(BaseModel):
    """
    types.PageBlockCollage
    ID: 0x65a0fa4d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockCollage'] = pydantic.Field(
        'types.PageBlockCollage',
        alias='_'
    )

    items: list["base.PageBlock"]
    caption: "base.PageCaption"
