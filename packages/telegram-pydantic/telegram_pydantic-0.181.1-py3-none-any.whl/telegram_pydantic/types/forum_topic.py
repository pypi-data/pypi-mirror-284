from __future__ import annotations

import typing

import pydantic

from telegram_pydantic.core import BaseModel

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ForumTopic(BaseModel):
    """
    types.ForumTopic
    ID: 0x71701da9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ForumTopic'] = pydantic.Field(
        'types.ForumTopic',
        alias='_'
    )

    id: int
    date: int
    title: str
    icon_color: int
    top_message: int
    read_inbox_max_id: int
    read_outbox_max_id: int
    unread_count: int
    unread_mentions_count: int
    unread_reactions_count: int
    from_id: "base.Peer"
    notify_settings: "base.PeerNotifySettings"
    my: typing.Optional[bool] = None
    closed: typing.Optional[bool] = None
    pinned: typing.Optional[bool] = None
    short: typing.Optional[bool] = None
    hidden: typing.Optional[bool] = None
    icon_emoji_id: typing.Optional[int] = None
    draft: typing.Optional["base.DraftMessage"] = None
