from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDocument(BaseModel):
    """
    types.InputDocument
    ID: 0x1abfb575
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDocument'] = pydantic.Field(
        'types.InputDocument',
        alias='_'
    )

    id: int
    access_hash: int
    file_reference: bytes
