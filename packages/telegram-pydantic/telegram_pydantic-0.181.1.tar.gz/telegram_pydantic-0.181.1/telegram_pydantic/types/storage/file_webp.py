from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileWebp(BaseModel):
    """
    types.storage.FileWebp
    ID: 0x1081464c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileWebp'] = pydantic.Field(
        'types.storage.FileWebp',
        alias='_'
    )

