from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SponsoredMessageReportOption - Layer 181
SponsoredMessageReportOption = typing.Annotated[
    typing.Union[
        types.SponsoredMessageReportOption
    ],
    pydantic.Field(discriminator='QUALNAME')
]
