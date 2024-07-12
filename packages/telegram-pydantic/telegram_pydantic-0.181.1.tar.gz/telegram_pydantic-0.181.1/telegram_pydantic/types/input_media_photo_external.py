from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPhotoExternal(BaseModel):
    """
    types.InputMediaPhotoExternal
    ID: 0xe5bbfe1a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPhotoExternal'] = pydantic.Field(
        'types.InputMediaPhotoExternal',
        alias='_'
    )

    url: str
    spoiler: typing.Optional[bool] = None
    ttl_seconds: typing.Optional[int] = None
