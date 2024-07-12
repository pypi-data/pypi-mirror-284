from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDocumentByHash(BaseModel):
    """
    functions.messages.GetDocumentByHash
    ID: 0xb1f2061f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetDocumentByHash'] = pydantic.Field(
        'functions.messages.GetDocumentByHash',
        alias='_'
    )

    sha256: bytes
    size: int
    mime_type: str
