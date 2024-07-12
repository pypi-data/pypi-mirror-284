from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetDefaultReaction(BaseModel):
    """
    functions.messages.SetDefaultReaction
    ID: 0x4f47a016
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetDefaultReaction'] = pydantic.Field(
        'functions.messages.SetDefaultReaction',
        alias='_'
    )

    reaction: "base.Reaction"
