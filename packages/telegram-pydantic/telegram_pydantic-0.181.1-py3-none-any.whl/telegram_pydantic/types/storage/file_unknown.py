from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileUnknown(BaseModel):
    """
    types.storage.FileUnknown
    ID: 0xaa963b05
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileUnknown'] = pydantic.Field(
        'types.storage.FileUnknown',
        alias='_'
    )

