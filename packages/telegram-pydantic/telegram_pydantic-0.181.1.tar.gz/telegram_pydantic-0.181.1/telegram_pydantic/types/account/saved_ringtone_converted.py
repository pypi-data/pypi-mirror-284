from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtoneConverted(BaseModel):
    """
    types.account.SavedRingtoneConverted
    ID: 0x1f307eb7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtoneConverted'] = pydantic.Field(
        'types.account.SavedRingtoneConverted',
        alias='_'
    )

    document: "base.Document"
