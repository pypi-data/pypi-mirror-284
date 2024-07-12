from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickeredMediaPhoto(BaseModel):
    """
    types.InputStickeredMediaPhoto
    ID: 0x4a992157
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickeredMediaPhoto'] = pydantic.Field(
        'types.InputStickeredMediaPhoto',
        alias='_'
    )

    id: "base.InputPhoto"
