from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FilePng(BaseModel):
    """
    types.storage.FilePng
    ID: 0xa4f63c0
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FilePng'] = pydantic.Field(
        'types.storage.FilePng',
        alias='_'
    )

