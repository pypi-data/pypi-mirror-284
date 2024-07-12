from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FilePartial(BaseModel):
    """
    types.storage.FilePartial
    ID: 0x40bc6f52
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FilePartial'] = pydantic.Field(
        'types.storage.FilePartial',
        alias='_'
    )

