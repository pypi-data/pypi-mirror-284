from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockChannel(BaseModel):
    """
    types.PageBlockChannel
    ID: 0xef1751b5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockChannel'] = pydantic.Field(
        'types.PageBlockChannel',
        alias='_'
    )

    channel: "base.Chat"
