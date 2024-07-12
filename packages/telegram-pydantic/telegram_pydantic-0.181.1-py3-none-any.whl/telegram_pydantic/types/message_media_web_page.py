from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageMediaWebPage(BaseModel):
    """
    types.MessageMediaWebPage
    ID: 0xddf10c3b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageMediaWebPage'] = pydantic.Field(
        'types.MessageMediaWebPage',
        alias='_'
    )

    webpage: "base.WebPage"
    force_large_media: typing.Optional[bool] = None
    force_small_media: typing.Optional[bool] = None
    manual: typing.Optional[bool] = None
    safe: typing.Optional[bool] = None
