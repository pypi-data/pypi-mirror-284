from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMessageReplyTo(BaseModel):
    """
    types.InputMessageReplyTo
    ID: 0xbad88395
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMessageReplyTo'] = pydantic.Field(
        'types.InputMessageReplyTo',
        alias='_'
    )

    id: int
