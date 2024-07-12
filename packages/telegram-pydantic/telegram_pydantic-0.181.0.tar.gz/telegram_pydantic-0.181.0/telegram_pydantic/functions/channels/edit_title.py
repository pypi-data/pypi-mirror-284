from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditTitle(BaseModel):
    """
    functions.channels.EditTitle
    ID: 0x566decd0
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditTitle'] = pydantic.Field(
        'functions.channels.EditTitle',
        alias='_'
    )

    channel: "base.InputChannel"
    title: str
