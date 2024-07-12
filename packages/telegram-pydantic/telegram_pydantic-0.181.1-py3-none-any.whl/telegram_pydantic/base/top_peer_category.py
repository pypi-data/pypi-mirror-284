from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# TopPeerCategory - Layer 181
TopPeerCategory = typing.Annotated[
    typing.Union[
        types.TopPeerCategoryBotsInline,
        types.TopPeerCategoryBotsPM,
        types.TopPeerCategoryChannels,
        types.TopPeerCategoryCorrespondents,
        types.TopPeerCategoryForwardChats,
        types.TopPeerCategoryForwardUsers,
        types.TopPeerCategoryGroups,
        types.TopPeerCategoryPhoneCalls
    ],
    pydantic.Field(discriminator='QUALNAME')
]
