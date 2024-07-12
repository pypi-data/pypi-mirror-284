from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportOption(BaseModel):
    """
    types.SponsoredMessageReportOption
    ID: 0x430d3150
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SponsoredMessageReportOption'] = pydantic.Field(
        'types.SponsoredMessageReportOption',
        alias='_'
    )

    text: str
    option: bytes
