from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputMedia - Layer 181
InputMedia = typing.Annotated[
    typing.Union[
        types.InputMediaContact,
        types.InputMediaDice,
        types.InputMediaDocument,
        types.InputMediaDocumentExternal,
        types.InputMediaEmpty,
        types.InputMediaGame,
        types.InputMediaGeoLive,
        types.InputMediaGeoPoint,
        types.InputMediaInvoice,
        types.InputMediaPhoto,
        types.InputMediaPhotoExternal,
        types.InputMediaPoll,
        types.InputMediaStory,
        types.InputMediaUploadedDocument,
        types.InputMediaUploadedPhoto,
        types.InputMediaVenue,
        types.InputMediaWebPage
    ],
    pydantic.Field(discriminator='QUALNAME')
]
