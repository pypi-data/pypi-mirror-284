from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class KeyboardButtonSwitchInline(BaseModel):
    """
    types.KeyboardButtonSwitchInline
    ID: 0x93b9fbb5
    Layer: 181
    """
    QUALNAME: typing.Literal['types.KeyboardButtonSwitchInline'] = pydantic.Field(
        'types.KeyboardButtonSwitchInline',
        alias='_'
    )

    text: str
    query: str
    same_peer: typing.Optional[bool] = None
    peer_types: typing.Optional[list["base.InlineQueryPeerType"]] = None
