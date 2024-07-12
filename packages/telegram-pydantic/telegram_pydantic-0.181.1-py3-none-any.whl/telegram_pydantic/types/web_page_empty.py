from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageEmpty(BaseModel):
    """
    types.WebPageEmpty
    ID: 0x211a1788
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageEmpty'] = pydantic.Field(
        'types.WebPageEmpty',
        alias='_'
    )

    id: int
    url: typing.Optional[str] = None
