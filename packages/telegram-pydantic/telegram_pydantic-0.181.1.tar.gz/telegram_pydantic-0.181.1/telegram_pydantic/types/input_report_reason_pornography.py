from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonPornography(BaseModel):
    """
    types.InputReportReasonPornography
    ID: 0x2e59d922
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonPornography'] = pydantic.Field(
        'types.InputReportReasonPornography',
        alias='_'
    )

