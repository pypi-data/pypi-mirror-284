from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedContactToken(BaseModel):
    """
    types.ExportedContactToken
    ID: 0x41bf109b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ExportedContactToken'] = pydantic.Field(
        'types.ExportedContactToken',
        alias='_'
    )

    url: str
    expires: int
