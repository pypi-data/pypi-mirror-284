from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedMessage(BaseModel):
    """
    functions.messages.UpdatePinnedMessage
    ID: 0xd2aaf7ec
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdatePinnedMessage'] = pydantic.Field(
        'functions.messages.UpdatePinnedMessage',
        alias='_'
    )

    peer: "base.InputPeer"
    id: int
    silent: typing.Optional[bool] = None
    unpin: typing.Optional[bool] = None
    pm_oneside: typing.Optional[bool] = None
