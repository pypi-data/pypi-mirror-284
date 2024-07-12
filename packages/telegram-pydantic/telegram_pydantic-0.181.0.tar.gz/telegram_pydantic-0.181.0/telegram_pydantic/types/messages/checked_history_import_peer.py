from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CheckedHistoryImportPeer(BaseModel):
    """
    types.messages.CheckedHistoryImportPeer
    ID: 0xa24de717
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.CheckedHistoryImportPeer'] = pydantic.Field(
        'types.messages.CheckedHistoryImportPeer',
        alias='_'
    )

    confirm_text: str
