from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonUrl(BaseModel):
    """
    types.KeyboardButtonUrl
    ID: 0x258aff05
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonUrl'] = pydantic.Field(
        'types.KeyboardButtonUrl',
        alias='_'
    )

    text: str
    url: str
