from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonUrlAuth(BaseModel):
    """
    types.KeyboardButtonUrlAuth
    ID: 0x10b78d29
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonUrlAuth'] = pydantic.Field(
        'types.KeyboardButtonUrlAuth',
        alias='_'
    )

    text: str
    url: str
    button_id: int
    fwd_text: typing.Optional[str] = None
