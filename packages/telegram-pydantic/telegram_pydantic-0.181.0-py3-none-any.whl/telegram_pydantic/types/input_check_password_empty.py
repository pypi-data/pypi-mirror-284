from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputCheckPasswordEmpty(BaseModel):
    """
    types.InputCheckPasswordEmpty
    ID: 0x9880f658
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputCheckPasswordEmpty'] = pydantic.Field(
        'types.InputCheckPasswordEmpty',
        alias='_'
    )

