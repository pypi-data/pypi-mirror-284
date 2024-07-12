from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUserSelf(BaseModel):
    """
    types.InputUserSelf
    ID: 0xf7c1b13f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUserSelf'] = pydantic.Field(
        'types.InputUserSelf',
        alias='_'
    )

