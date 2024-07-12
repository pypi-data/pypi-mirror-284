from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateTheme(BaseModel):
    """
    functions.account.UpdateTheme
    ID: 0x2bf40ccc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.UpdateTheme'] = pydantic.Field(
        'functions.account.UpdateTheme',
        alias='_'
    )

    format: str
    theme: "base.InputTheme"
    slug: typing.Optional[str] = None
    title: typing.Optional[str] = None
    document: typing.Optional["base.InputDocument"] = None
    settings: typing.Optional[list["base.InputThemeSettings"]] = None
