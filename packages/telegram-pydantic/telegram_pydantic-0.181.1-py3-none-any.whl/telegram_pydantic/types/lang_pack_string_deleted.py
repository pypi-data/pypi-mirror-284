from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackStringDeleted(BaseModel):
    """
    types.LangPackStringDeleted
    ID: 0x2979eeb2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackStringDeleted'] = pydantic.Field(
        'types.LangPackStringDeleted',
        alias='_'
    )

    key: str
