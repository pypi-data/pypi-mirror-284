from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckHistoryImport(BaseModel):
    """
    functions.messages.CheckHistoryImport
    ID: 0x43fe19f3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.CheckHistoryImport'] = pydantic.Field(
        'functions.messages.CheckHistoryImport',
        alias='_'
    )

    import_head: str
