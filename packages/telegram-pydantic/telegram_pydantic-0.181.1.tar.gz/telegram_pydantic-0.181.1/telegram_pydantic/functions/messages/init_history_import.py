from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InitHistoryImport(BaseModel):
    """
    functions.messages.InitHistoryImport
    ID: 0x34090c3b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.InitHistoryImport'] = pydantic.Field(
        'functions.messages.InitHistoryImport',
        alias='_'
    )

    peer: "base.InputPeer"
    file: "base.InputFile"
    media_count: int
