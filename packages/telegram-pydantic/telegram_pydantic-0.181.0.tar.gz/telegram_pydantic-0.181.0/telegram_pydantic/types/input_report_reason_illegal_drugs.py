from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonIllegalDrugs(BaseModel):
    """
    types.InputReportReasonIllegalDrugs
    ID: 0xa8eb2be
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonIllegalDrugs'] = pydantic.Field(
        'types.InputReportReasonIllegalDrugs',
        alias='_'
    )

