from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DismissSuggestion(BaseModel):
    """
    functions.help.DismissSuggestion
    ID: 0xf50dbaa1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.DismissSuggestion'] = pydantic.Field(
        'functions.help.DismissSuggestion',
        alias='_'
    )

    peer: "base.InputPeer"
    suggestion: str
