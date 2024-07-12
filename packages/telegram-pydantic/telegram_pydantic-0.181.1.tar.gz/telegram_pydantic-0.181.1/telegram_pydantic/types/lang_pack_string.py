from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackString(BaseModel):
    """
    types.LangPackString
    ID: 0xcad181f6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackString'] = pydantic.Field(
        'types.LangPackString',
        alias='_'
    )

    key: str
    value: str
