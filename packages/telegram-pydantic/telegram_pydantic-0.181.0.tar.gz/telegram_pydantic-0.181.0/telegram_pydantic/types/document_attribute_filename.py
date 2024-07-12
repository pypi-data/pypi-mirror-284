from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DocumentAttributeFilename(BaseModel):
    """
    types.DocumentAttributeFilename
    ID: 0x15590068
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DocumentAttributeFilename'] = pydantic.Field(
        'types.DocumentAttributeFilename',
        alias='_'
    )

    file_name: str
