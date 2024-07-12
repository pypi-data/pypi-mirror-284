from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNotifySettings(BaseModel):
    """
    types.UpdateNotifySettings
    ID: 0xbec268ef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNotifySettings'] = pydantic.Field(
        'types.UpdateNotifySettings',
        alias='_'
    )

    peer: "base.NotifyPeer"
    notify_settings: "base.PeerNotifySettings"
