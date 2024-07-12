from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AllStickersNotModified(BaseModel):
    """
    types.messages.AllStickersNotModified
    ID: 0xe86602c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AllStickersNotModified'] = pydantic.Field(
        'types.messages.AllStickersNotModified',
        alias='_'
    )

