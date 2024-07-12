from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveGif(BaseModel):
    """
    functions.messages.SaveGif
    ID: 0x327a30cb
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SaveGif'] = pydantic.Field(
        'functions.messages.SaveGif',
        alias='_'
    )

    id: "base.InputDocument"
    unsave: bool
