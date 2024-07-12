from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaEmpty(BaseModel):
    """
    types.InputMediaEmpty
    ID: 0x9664f57f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaEmpty'] = pydantic.Field(
        'types.InputMediaEmpty',
        alias='_'
    )

