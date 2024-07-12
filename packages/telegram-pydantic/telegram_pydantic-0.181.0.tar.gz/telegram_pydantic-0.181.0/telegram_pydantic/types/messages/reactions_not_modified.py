from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionsNotModified(BaseModel):
    """
    types.messages.ReactionsNotModified
    ID: 0xb06fdbdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ReactionsNotModified'] = pydantic.Field(
        'types.messages.ReactionsNotModified',
        alias='_'
    )

