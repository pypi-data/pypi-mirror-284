from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Theme(BaseModel):
    """
    types.Theme
    ID: 0xa00e67d6
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Theme'] = pydantic.Field(
        'types.Theme',
        alias='_'
    )

    id: int
    access_hash: int
    slug: str
    title: str
    creator: typing.Optional[bool] = None
    default: typing.Optional[bool] = None
    for_chat: typing.Optional[bool] = None
    document: typing.Optional["base.Document"] = None
    settings: typing.Optional[list["base.ThemeSettings"]] = None
    emoticon: typing.Optional[str] = None
    installs_count: typing.Optional[int] = None
