from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonViolence(BaseModel):
    """
    types.InputReportReasonViolence
    ID: 0x1e22c78d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonViolence'] = pydantic.Field(
        'types.InputReportReasonViolence',
        alias='_'
    )

