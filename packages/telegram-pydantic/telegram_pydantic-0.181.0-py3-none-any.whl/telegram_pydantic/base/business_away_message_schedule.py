from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessAwayMessageSchedule - Layer 181
BusinessAwayMessageSchedule = typing.Annotated[
    typing.Union[
        types.BusinessAwayMessageScheduleAlways,
        types.BusinessAwayMessageScheduleCustom,
        types.BusinessAwayMessageScheduleOutsideWorkHours
    ],
    pydantic.Field(discriminator='QUALNAME')
]
