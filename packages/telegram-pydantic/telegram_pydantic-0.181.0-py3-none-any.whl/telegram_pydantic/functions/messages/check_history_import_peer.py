from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckHistoryImportPeer(BaseModel):
    """
    functions.messages.CheckHistoryImportPeer
    ID: 0x5dc60f03
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckHistoryImportPeer'] = pydantic.Field(
        'functions.messages.CheckHistoryImportPeer',
        alias='_'
    )

    peer: "base.InputPeer"
