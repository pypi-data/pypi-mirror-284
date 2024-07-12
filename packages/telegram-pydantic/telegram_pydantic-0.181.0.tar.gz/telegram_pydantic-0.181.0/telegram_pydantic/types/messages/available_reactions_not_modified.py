from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableReactionsNotModified(BaseModel):
    """
    types.messages.AvailableReactionsNotModified
    ID: 0x9f071957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableReactionsNotModified'] = pydantic.Field(
        'types.messages.AvailableReactionsNotModified',
        alias='_'
    )

