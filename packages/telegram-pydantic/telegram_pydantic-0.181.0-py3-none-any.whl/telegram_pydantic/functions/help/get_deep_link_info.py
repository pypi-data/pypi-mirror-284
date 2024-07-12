from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetDeepLinkInfo(BaseModel):
    """
    functions.help.GetDeepLinkInfo
    ID: 0x3fedc75f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetDeepLinkInfo'] = pydantic.Field(
        'functions.help.GetDeepLinkInfo',
        alias='_'
    )

    path: str
