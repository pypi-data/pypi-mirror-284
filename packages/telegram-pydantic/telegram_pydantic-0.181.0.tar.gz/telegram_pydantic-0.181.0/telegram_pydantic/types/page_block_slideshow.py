from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockSlideshow(BaseModel):
    """
    types.PageBlockSlideshow
    ID: 0x31f9590
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockSlideshow'] = pydantic.Field(
        'types.PageBlockSlideshow',
        alias='_'
    )

    items: list["base.PageBlock"]
    caption: "base.PageCaption"
