from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CountriesListNotModified(BaseModel):
    """
    types.help.CountriesListNotModified
    ID: 0x93cc1f32
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.CountriesListNotModified'] = pydantic.Field(
        'types.help.CountriesListNotModified',
        alias='_'
    )

