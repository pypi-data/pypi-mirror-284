from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWebPagePreview(BaseModel):
    """
    functions.messages.GetWebPagePreview
    ID: 0x8b68b0cc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetWebPagePreview'] = pydantic.Field(
        'functions.messages.GetWebPagePreview',
        alias='_'
    )

    message: str
    entities: typing.Optional[list["base.MessageEntity"]] = None
