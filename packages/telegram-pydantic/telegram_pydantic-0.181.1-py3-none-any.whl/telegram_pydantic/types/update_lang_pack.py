from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateLangPack(BaseModel):
    """
    types.UpdateLangPack
    ID: 0x56022f4d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateLangPack'] = pydantic.Field(
        'types.UpdateLangPack',
        alias='_'
    )

    difference: "base.LangPackDifference"
