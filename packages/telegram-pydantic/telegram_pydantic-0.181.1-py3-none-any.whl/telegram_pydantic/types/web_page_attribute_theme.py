from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeTheme(BaseModel):
    """
    types.WebPageAttributeTheme
    ID: 0x54b56617
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeTheme'] = pydantic.Field(
        'types.WebPageAttributeTheme',
        alias='_'
    )

    documents: typing.Optional[list["base.Document"]] = None
    settings: typing.Optional["base.ThemeSettings"] = None
