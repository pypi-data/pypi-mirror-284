from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HidePeerSettingsBar(BaseModel):
    """
    functions.messages.HidePeerSettingsBar
    ID: 0x4facb138
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HidePeerSettingsBar'] = pydantic.Field(
        'functions.messages.HidePeerSettingsBar',
        alias='_'
    )

    peer: "base.InputPeer"
