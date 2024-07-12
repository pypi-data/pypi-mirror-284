from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessageReportResultChooseOption(BaseModel):
    """
    types.channels.SponsoredMessageReportResultChooseOption
    ID: 0x846f9e42
    Layer: 181
    """
    QUALNAME: typing.Literal['types.channels.SponsoredMessageReportResultChooseOption'] = pydantic.Field(
        'types.channels.SponsoredMessageReportResultChooseOption',
        alias='_'
    )

    title: str
    options: list["base.SponsoredMessageReportOption"]
