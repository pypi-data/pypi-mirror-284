from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebDocumentNoProxy(BaseModel):
    """
    types.WebDocumentNoProxy
    ID: 0xf9c8bcc6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebDocumentNoProxy'] = pydantic.Field(
        'types.WebDocumentNoProxy',
        alias='_'
    )

    url: str
    size: int
    mime_type: str
    attributes: list["base.DocumentAttribute"]
