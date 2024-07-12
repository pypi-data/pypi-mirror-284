from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetRecentMeUrls(BaseModel):
    """
    functions.help.GetRecentMeUrls
    ID: 0x3dc0f114
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetRecentMeUrls'] = pydantic.Field(
        'functions.help.GetRecentMeUrls',
        alias='_'
    )

    referer: str
