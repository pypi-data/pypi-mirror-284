from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockPreformatted(BaseModel):
    """
    types.PageBlockPreformatted
    ID: 0xc070d93e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockPreformatted'] = pydantic.Field(
        'types.PageBlockPreformatted',
        alias='_'
    )

    text: "base.RichText"
    language: str
