from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaDocument(BaseModel):
    """
    types.InputMediaDocument
    ID: 0x33473058
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaDocument'] = pydantic.Field(
        'types.InputMediaDocument',
        alias='_'
    )

    id: "base.InputDocument"
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
    query: typing.Optional[str] = None
