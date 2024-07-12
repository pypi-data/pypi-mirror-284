from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonGeoIrrelevant(BaseModel):
    """
    types.InputReportReasonGeoIrrelevant
    ID: 0xdbd4feed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonGeoIrrelevant'] = pydantic.Field(
        'types.InputReportReasonGeoIrrelevant',
        alias='_'
    )

