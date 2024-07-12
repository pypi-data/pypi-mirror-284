from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessagesFilterGeo(BaseModel):
    """
    types.InputMessagesFilterGeo
    ID: 0xe7026d0d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessagesFilterGeo'] = pydantic.Field(
        'types.InputMessagesFilterGeo',
        alias='_'
    )

