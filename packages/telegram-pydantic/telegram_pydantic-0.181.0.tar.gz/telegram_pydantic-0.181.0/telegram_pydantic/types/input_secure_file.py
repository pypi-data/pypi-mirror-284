from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputSecureFile(BaseModel):
    """
    types.InputSecureFile
    ID: 0x5367e5be
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputSecureFile'] = pydantic.Field(
        'types.InputSecureFile',
        alias='_'
    )

    id: int
    access_hash: int
