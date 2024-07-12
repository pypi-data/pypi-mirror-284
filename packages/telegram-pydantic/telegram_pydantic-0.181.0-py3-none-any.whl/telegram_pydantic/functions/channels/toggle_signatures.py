from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleSignatures(BaseModel):
    """
    functions.channels.ToggleSignatures
    ID: 0x1f69b606
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.ToggleSignatures'] = pydantic.Field(
        'functions.channels.ToggleSignatures',
        alias='_'
    )

    channel: "base.InputChannel"
    enabled: bool
