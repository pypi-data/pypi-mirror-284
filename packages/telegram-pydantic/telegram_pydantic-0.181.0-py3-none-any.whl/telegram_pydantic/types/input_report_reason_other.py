from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonOther(BaseModel):
    """
    types.InputReportReasonOther
    ID: 0xc1e4a2b1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonOther'] = pydantic.Field(
        'types.InputReportReasonOther',
        alias='_'
    )

