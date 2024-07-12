from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DialogFilterSuggested - Layer 181
DialogFilterSuggested = typing.Annotated[
    typing.Union[
        types.DialogFilterSuggested
    ],
    pydantic.Field(discriminator='QUALNAME')
]
