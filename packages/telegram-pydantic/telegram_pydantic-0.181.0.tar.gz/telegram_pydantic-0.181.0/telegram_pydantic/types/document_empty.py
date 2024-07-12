from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentEmpty(BaseModel):
    """
    types.DocumentEmpty
    ID: 0x36f8c871
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentEmpty'] = pydantic.Field(
        'types.DocumentEmpty',
        alias='_'
    )

    id: int
