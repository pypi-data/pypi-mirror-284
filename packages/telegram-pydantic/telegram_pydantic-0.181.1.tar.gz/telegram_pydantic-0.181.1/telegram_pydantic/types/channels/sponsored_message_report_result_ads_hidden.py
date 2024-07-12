from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportResultAdsHidden(BaseModel):
    """
    types.channels.SponsoredMessageReportResultAdsHidden
    ID: 0x3e3bcf2f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SponsoredMessageReportResultAdsHidden'] = pydantic.Field(
        'types.channels.SponsoredMessageReportResultAdsHidden',
        alias='_'
    )

