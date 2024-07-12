from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReportReason - Layer 181
ReportReason = typing.Annotated[
    typing.Union[
        types.InputReportReasonChildAbuse,
        types.InputReportReasonCopyright,
        types.InputReportReasonFake,
        types.InputReportReasonGeoIrrelevant,
        types.InputReportReasonIllegalDrugs,
        types.InputReportReasonOther,
        types.InputReportReasonPersonalDetails,
        types.InputReportReasonPornography,
        types.InputReportReasonSpam,
        types.InputReportReasonViolence
    ],
    pydantic.Field(discriminator='QUALNAME')
]
