from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Country(BaseModel):
    """
    types.help.Country
    ID: 0xc3878e23
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.Country'] = pydantic.Field(
        'types.help.Country',
        alias='_'
    )

    iso2: str
    default_name: str
    country_codes: list["base.help.CountryCode"]
    hidden: typing.Optional[bool] = None
    name: typing.Optional[str] = None
