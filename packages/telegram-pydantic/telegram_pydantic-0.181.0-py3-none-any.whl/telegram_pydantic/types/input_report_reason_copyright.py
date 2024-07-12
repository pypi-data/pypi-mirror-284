from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputReportReasonCopyright(BaseModel):
    """
    types.InputReportReasonCopyright
    ID: 0x9b89f93a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputReportReasonCopyright'] = pydantic.Field(
        'types.InputReportReasonCopyright',
        alias='_'
    )

