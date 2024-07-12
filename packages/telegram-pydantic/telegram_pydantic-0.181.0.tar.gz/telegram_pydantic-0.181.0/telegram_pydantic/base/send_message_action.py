from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SendMessageAction - Layer 181
SendMessageAction = typing.Annotated[
    typing.Union[
        types.SendMessageCancelAction,
        types.SendMessageChooseContactAction,
        types.SendMessageChooseStickerAction,
        types.SendMessageEmojiInteraction,
        types.SendMessageEmojiInteractionSeen,
        types.SendMessageGamePlayAction,
        types.SendMessageGeoLocationAction,
        types.SendMessageHistoryImportAction,
        types.SendMessageRecordAudioAction,
        types.SendMessageRecordRoundAction,
        types.SendMessageRecordVideoAction,
        types.SendMessageTypingAction,
        types.SendMessageUploadAudioAction,
        types.SendMessageUploadDocumentAction,
        types.SendMessageUploadPhotoAction,
        types.SendMessageUploadRoundAction,
        types.SendMessageUploadVideoAction,
        types.SpeakingInGroupCallAction
    ],
    pydantic.Field(discriminator='QUALNAME')
]
