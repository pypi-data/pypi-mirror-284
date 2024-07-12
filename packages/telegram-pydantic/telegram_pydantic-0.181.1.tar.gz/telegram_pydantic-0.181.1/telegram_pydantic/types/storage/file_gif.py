from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FileGif(BaseModel):
    """
    types.storage.FileGif
    ID: 0xcae1aadf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FileGif'] = pydantic.Field(
        'types.storage.FileGif',
        alias='_'
    )

