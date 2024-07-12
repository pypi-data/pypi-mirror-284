from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWebDocument(BaseModel):
    """
    types.InputWebDocument
    ID: 0x9bed434d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWebDocument'] = pydantic.Field(
        'types.InputWebDocument',
        alias='_'
    )

    url: str
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
