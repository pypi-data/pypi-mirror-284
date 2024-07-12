from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SuggestedShortName(BaseModel):
    """
    types.stickers.SuggestedShortName
    ID: 0x85fea03f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.stickers.SuggestedShortName'] = pydantic.Field(
        'types.stickers.SuggestedShortName',
        alias='_'
    )

    short_name: str
