from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportResultReported(BaseModel):
    """
    types.channels.SponsoredMessageReportResultReported
    ID: 0xad798849
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SponsoredMessageReportResultReported'] = pydantic.Field(
        'types.channels.SponsoredMessageReportResultReported',
        alias='_'
    )

