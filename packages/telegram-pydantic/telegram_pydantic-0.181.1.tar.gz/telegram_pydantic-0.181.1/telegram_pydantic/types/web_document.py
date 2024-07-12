from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebDocument(BaseModel):
    """
    types.WebDocument
    ID: 0x1c570ed1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebDocument'] = pydantic.Field(
        'types.WebDocument',
        alias='_'
    )

    url: str
    access_hash: int
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
