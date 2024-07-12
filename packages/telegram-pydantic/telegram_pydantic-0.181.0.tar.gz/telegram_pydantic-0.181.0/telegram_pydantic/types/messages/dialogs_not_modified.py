from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogsNotModified(BaseModel):
    """
    types.messages.DialogsNotModified
    ID: 0xf0e3e596
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DialogsNotModified'] = pydantic.Field(
        'types.messages.DialogsNotModified',
        alias='_'
    )

    count: int
