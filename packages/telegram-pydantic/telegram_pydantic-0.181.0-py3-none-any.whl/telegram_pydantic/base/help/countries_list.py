from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.CountriesList - Layer 181
CountriesList = typing.Annotated[
    typing.Union[
        types.help.CountriesList,
        types.help.CountriesListNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
