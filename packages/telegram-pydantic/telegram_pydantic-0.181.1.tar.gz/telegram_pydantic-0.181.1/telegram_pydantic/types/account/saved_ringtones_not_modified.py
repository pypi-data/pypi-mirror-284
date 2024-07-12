from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SavedRingtonesNotModified(BaseModel):
    """
    types.account.SavedRingtonesNotModified
    ID: 0xfbf6e8b1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.SavedRingtonesNotModified'] = pydantic.Field(
        'types.account.SavedRingtonesNotModified',
        alias='_'
    )

