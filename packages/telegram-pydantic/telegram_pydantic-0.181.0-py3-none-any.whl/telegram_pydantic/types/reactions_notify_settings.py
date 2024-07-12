from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionsNotifySettings(BaseModel):
    """
    types.ReactionsNotifySettings
    ID: 0x56e34970
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReactionsNotifySettings'] = pydantic.Field(
        'types.ReactionsNotifySettings',
        alias='_'
    )

    sound: "base.NotificationSound"
    show_previews: bool
    messages_notify_from: typing.Optional["base.ReactionNotificationsFrom"] = None
    stories_notify_from: typing.Optional["base.ReactionNotificationsFrom"] = None
