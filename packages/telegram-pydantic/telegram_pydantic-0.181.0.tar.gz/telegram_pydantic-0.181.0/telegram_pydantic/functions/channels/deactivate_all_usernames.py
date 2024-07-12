from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeactivateAllUsernames(BaseModel):
    """
    functions.channels.DeactivateAllUsernames
    ID: 0xa245dd3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeactivateAllUsernames'] = pydantic.Field(
        'functions.channels.DeactivateAllUsernames',
        alias='_'
    )

    channel: "base.InputChannel"
