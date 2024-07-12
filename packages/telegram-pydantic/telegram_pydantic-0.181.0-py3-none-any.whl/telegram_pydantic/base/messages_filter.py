from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessagesFilter - Layer 181
MessagesFilter = typing.Annotated[
    typing.Union[
        types.InputMessagesFilterChatPhotos,
        types.InputMessagesFilterContacts,
        types.InputMessagesFilterDocument,
        types.InputMessagesFilterEmpty,
        types.InputMessagesFilterGeo,
        types.InputMessagesFilterGif,
        types.InputMessagesFilterMusic,
        types.InputMessagesFilterMyMentions,
        types.InputMessagesFilterPhoneCalls,
        types.InputMessagesFilterPhotoVideo,
        types.InputMessagesFilterPhotos,
        types.InputMessagesFilterPinned,
        types.InputMessagesFilterRoundVideo,
        types.InputMessagesFilterRoundVoice,
        types.InputMessagesFilterUrl,
        types.InputMessagesFilterVideo,
        types.InputMessagesFilterVoice
    ],
    pydantic.Field(discriminator='QUALNAME')
]
