from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# RecentMeUrl - Layer 181
RecentMeUrl = typing.Annotated[
    typing.Union[
        types.RecentMeUrlChat,
        types.RecentMeUrlChatInvite,
        types.RecentMeUrlStickerSet,
        types.RecentMeUrlUnknown,
        types.RecentMeUrlUser
    ],
    pydantic.Field(discriminator='QUALNAME')
]
