from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InstallTheme(BaseModel):
    """
    functions.account.InstallTheme
    ID: 0xc727bb3b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InstallTheme'] = pydantic.Field(
        'functions.account.InstallTheme',
        alias='_'
    )

    dark: typing.Optional[bool] = None
    theme: typing.Optional["base.InputTheme"] = None
    format: typing.Optional[str] = None
    base_theme: typing.Optional["base.BaseTheme"] = None
