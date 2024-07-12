from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPhoto(BaseModel):
    """
    types.InputMediaPhoto
    ID: 0xb3ba0635
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPhoto'] = pydantic.Field(
        'types.InputMediaPhoto',
        alias='_'
    )

    id: "base.InputPhoto"
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
