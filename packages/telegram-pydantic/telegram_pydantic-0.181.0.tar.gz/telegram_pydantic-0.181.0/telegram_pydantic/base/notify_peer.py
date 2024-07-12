from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# NotifyPeer - Layer 181
NotifyPeer = typing.Annotated[
    typing.Union[
        types.NotifyBroadcasts,
        types.NotifyChats,
        types.NotifyForumTopic,
        types.NotifyPeer,
        types.NotifyUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
