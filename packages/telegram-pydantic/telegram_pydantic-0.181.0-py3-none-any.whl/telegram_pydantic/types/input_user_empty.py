from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputUserEmpty(BaseModel):
    """
    types.InputUserEmpty
    ID: 0xb98886cf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputUserEmpty'] = pydantic.Field(
        'types.InputUserEmpty',
        alias='_'
    )

