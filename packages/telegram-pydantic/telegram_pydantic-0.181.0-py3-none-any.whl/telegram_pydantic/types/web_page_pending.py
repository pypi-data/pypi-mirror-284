from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPagePending(BaseModel):
    """
    types.WebPagePending
    ID: 0xb0d13e47
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPagePending'] = pydantic.Field(
        'types.WebPagePending',
        alias='_'
    )

    id: int
    date: int
    url: typing.Optional[str] = None
