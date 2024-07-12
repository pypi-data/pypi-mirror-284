from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class LangPackDifference(BaseModel):
    """
    types.LangPackDifference
    ID: 0xf385c1f6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.LangPackDifference'] = pydantic.Field(
        'types.LangPackDifference',
        alias='_'
    )

    lang_code: str
    from_version: int
    version: int
    strings: list["base.LangPackString"]
