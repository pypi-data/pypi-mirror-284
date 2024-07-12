from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveRecentSticker(BaseModel):
    """
    functions.messages.SaveRecentSticker
    ID: 0x392718f8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SaveRecentSticker'] = pydantic.Field(
        'functions.messages.SaveRecentSticker',
        alias='_'
    )

    id: "base.InputDocument"
    unsave: bool
    attached: typing.Optional[bool] = None
