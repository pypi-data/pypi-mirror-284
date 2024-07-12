from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocumentFileLocation(BaseModel):
    """
    types.InputDocumentFileLocation
    ID: 0xbad07584
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocumentFileLocation'] = pydantic.Field(
        'types.InputDocumentFileLocation',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: bytes
    thumb_size: str
