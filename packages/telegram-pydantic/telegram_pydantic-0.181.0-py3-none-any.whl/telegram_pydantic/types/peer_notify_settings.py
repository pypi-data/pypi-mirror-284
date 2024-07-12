from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerNotifySettings(BaseModel):
    """
    types.PeerNotifySettings
    ID: 0x99622c0c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PeerNotifySettings'] = pydantic.Field(
        'types.PeerNotifySettings',
        alias='_'
    )

    show_previews: typing.Optional[bool] = None
    silent: typing.Optional[bool] = None
    mute_until: typing.Optional[int] = None
    ios_sound: typing.Optional["base.NotificationSound"] = None
    android_sound: typing.Optional["base.NotificationSound"] = None
    other_sound: typing.Optional["base.NotificationSound"] = None
    stories_muted: typing.Optional[bool] = None
    stories_hide_sender: typing.Optional[bool] = None
    stories_ios_sound: typing.Optional["base.NotificationSound"] = None
    stories_android_sound: typing.Optional["base.NotificationSound"] = None
    stories_other_sound: typing.Optional["base.NotificationSound"] = None
