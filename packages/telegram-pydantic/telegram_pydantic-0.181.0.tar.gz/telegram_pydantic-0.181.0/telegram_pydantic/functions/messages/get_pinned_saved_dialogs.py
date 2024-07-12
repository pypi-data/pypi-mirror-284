from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPinnedSavedDialogs(BaseModel):
    """
    functions.messages.GetPinnedSavedDialogs
    ID: 0xd63d94e0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPinnedSavedDialogs'] = pydantic.Field(
        'functions.messages.GetPinnedSavedDialogs',
        alias='_'
    )

