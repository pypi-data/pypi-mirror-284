from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonSpam(BaseModel):
    """
    types.InputReportReasonSpam
    ID: 0x58dbcab8
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonSpam'] = pydantic.Field(
        'types.InputReportReasonSpam',
        alias='_'
    )

