from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonFake(BaseModel):
    """
    types.InputReportReasonFake
    ID: 0xf5ddd6e7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonFake'] = pydantic.Field(
        'types.InputReportReasonFake',
        alias='_'
    )

