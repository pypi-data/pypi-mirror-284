from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessagesEmpty(BaseModel):
    """
    types.messages.SponsoredMessagesEmpty
    ID: 0x1839490f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SponsoredMessagesEmpty'] = pydantic.Field(
        'types.messages.SponsoredMessagesEmpty',
        alias='_'
    )

