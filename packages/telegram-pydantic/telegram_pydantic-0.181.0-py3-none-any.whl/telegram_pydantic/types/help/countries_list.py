from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CountriesList(BaseModel):
    """
    types.help.CountriesList
    ID: 0x87d0759e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.CountriesList'] = pydantic.Field(
        'types.help.CountriesList',
        alias='_'
    )

    countries: list["base.help.Country"]
    hash: int
