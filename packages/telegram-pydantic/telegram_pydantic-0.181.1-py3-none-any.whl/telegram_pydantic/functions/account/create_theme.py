from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CreateTheme(BaseModel):
    """
    functions.account.CreateTheme
    ID: 0x652e4400
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.CreateTheme'] = pydantic.Field(
        'functions.account.CreateTheme',
        alias='_'
    )

    slug: str
    title: str
    document: typing.Optional["base.InputDocument"] = None
    settings: typing.Optional[list["base.InputThemeSettings"]] = None
