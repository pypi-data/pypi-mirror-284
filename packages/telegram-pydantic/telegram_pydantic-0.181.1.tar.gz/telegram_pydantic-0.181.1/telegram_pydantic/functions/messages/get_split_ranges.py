from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSplitRanges(BaseModel):
    """
    functions.messages.GetSplitRanges
    ID: 0x1cff7e08
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSplitRanges'] = pydantic.Field(
        'functions.messages.GetSplitRanges',
        alias='_'
    )

