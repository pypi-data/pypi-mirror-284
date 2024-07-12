from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureFileLocation(BaseModel):
    """
    types.InputSecureFileLocation
    ID: 0xcbc7ee28
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureFileLocation'] = pydantic.Field(
        'types.InputSecureFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
