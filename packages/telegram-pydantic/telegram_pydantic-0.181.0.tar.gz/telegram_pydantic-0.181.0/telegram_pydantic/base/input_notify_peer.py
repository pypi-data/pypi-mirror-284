from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputNotifyPeer - Layer 181
InputNotifyPeer = typing.Annotated[
    typing.Union[
        types.InputNotifyBroadcasts,
        types.InputNotifyChats,
        types.InputNotifyForumTopic,
        types.InputNotifyPeer,
        types.InputNotifyUsers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
