from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileMp3(BaseModel):
    """
    types.storage.FileMp3
    ID: 0x528a0677
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileMp3'] = pydantic.Field(
        'types.storage.FileMp3',
        alias='_'
    )

