from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonChildAbuse(BaseModel):
    """
    types.InputReportReasonChildAbuse
    ID: 0xadf44ee3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonChildAbuse'] = pydantic.Field(
        'types.InputReportReasonChildAbuse',
        alias='_'
    )

