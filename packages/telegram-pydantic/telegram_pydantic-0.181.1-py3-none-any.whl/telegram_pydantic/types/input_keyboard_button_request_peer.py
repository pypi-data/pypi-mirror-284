from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputKeyboardButtonRequestPeer(BaseModel):
    """
    types.InputKeyboardButtonRequestPeer
    ID: 0xc9662d05
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputKeyboardButtonRequestPeer'] = pydantic.Field(
        'types.InputKeyboardButtonRequestPeer',
        alias='_'
    )

    text: str
    button_id: int
    peer_type: "base.RequestPeerType"
    max_quantity: int
    name_requested: typing.Optional[bool] = None
    username_requested: typing.Optional[bool] = None
    photo_requested: typing.Optional[bool] = None
