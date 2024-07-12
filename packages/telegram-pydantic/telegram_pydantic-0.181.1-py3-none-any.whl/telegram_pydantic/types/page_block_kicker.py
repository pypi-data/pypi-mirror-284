from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockKicker(BaseModel):
    """
    types.PageBlockKicker
    ID: 0x1e148390
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockKicker'] = pydantic.Field(
        'types.PageBlockKicker',
        alias='_'
    )

    text: "base.RichText"
