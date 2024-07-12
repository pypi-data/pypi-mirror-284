from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FilePdf(BaseModel):
    """
    types.storage.FilePdf
    ID: 0xae1e508d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.storage.FilePdf'] = pydantic.Field(
        'types.storage.FilePdf',
        alias='_'
    )

