from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveTheme(BaseModel):
    """
    functions.account.SaveTheme
    ID: 0xf257106c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveTheme'] = pydantic.Field(
        'functions.account.SaveTheme',
        alias='_'
    )

    theme: "base.InputTheme"
    unsave: bool
