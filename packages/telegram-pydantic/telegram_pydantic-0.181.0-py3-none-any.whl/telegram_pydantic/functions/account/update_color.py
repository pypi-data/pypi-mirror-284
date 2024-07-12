from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateColor(BaseModel):
    """
    functions.account.UpdateColor
    ID: 0x7cefa15d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateColor'] = pydantic.Field(
        'functions.account.UpdateColor',
        alias='_'
    )

    for_profile: typing.Optional[bool] = None
    color: typing.Optional[int] = None
    background_emoji_id: typing.Optional[int] = None
