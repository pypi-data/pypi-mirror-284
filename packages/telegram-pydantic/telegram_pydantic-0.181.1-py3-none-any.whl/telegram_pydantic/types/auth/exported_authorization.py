from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedAuthorization(BaseModel):
    """
    types.auth.ExportedAuthorization
    ID: 0xb434e2b8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.ExportedAuthorization'] = pydantic.Field(
        'types.auth.ExportedAuthorization',
        alias='_'
    )

    id: int
    bytes: bytes
