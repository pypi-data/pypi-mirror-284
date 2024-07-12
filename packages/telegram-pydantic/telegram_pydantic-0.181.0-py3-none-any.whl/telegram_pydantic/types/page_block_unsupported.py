from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockUnsupported(BaseModel):
    """
    types.PageBlockUnsupported
    ID: 0x13567e8a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockUnsupported'] = pydantic.Field(
        'types.PageBlockUnsupported',
        alias='_'
    )

