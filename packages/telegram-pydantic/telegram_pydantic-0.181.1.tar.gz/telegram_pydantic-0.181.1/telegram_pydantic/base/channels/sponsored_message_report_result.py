from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# channels.SponsoredMessageReportResult - Layer 181
SponsoredMessageReportResult = typing.Annotated[
    typing.Union[
        types.channels.SponsoredMessageReportResultAdsHidden,
        types.channels.SponsoredMessageReportResultChooseOption,
        types.channels.SponsoredMessageReportResultReported
    ],
    pydantic.Field(discriminator='QUALNAME')
]
