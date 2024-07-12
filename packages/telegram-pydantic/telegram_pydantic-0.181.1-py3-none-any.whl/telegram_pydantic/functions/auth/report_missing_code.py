from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReportMissingCode(BaseModel):
    """
    functions.auth.ReportMissingCode
    ID: 0xcb9deff6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ReportMissingCode'] = pydantic.Field(
        'functions.auth.ReportMissingCode',
        alias='_'
    )

    phone_number: str
    phone_code_hash: str
    mnc: str
