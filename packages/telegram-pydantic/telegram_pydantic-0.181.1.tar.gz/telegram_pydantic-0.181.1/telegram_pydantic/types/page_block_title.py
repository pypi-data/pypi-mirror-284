from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockTitle(BaseModel):
    """
    types.PageBlockTitle
    ID: 0x70abc3fd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockTitle'] = pydantic.Field(
        'types.PageBlockTitle',
        alias='_'
    )

    text: "base.RichText"
