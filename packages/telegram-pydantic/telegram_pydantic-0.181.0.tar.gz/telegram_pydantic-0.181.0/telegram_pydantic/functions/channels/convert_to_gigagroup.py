from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ConvertToGigagroup(BaseModel):
    """
    functions.channels.ConvertToGigagroup
    ID: 0xb290c69
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ConvertToGigagroup'] = pydantic.Field(
        'functions.channels.ConvertToGigagroup',
        alias='_'
    )

    channel: "base.InputChannel"
