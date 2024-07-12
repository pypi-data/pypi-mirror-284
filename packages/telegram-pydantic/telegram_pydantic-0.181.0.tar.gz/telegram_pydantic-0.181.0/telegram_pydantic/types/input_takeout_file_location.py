from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputTakeoutFileLocation(BaseModel):
    """
    types.InputTakeoutFileLocation
    ID: 0x29be5899
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputTakeoutFileLocation'] = pydantic.Field(
        'types.InputTakeoutFileLocation',
        alias='_'
    )

