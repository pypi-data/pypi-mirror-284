from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputFileLocation - Layer 181
InputFileLocation = typing.Annotated[
    typing.Union[
        types.InputDocumentFileLocation,
        types.InputEncryptedFileLocation,
        types.InputFileLocation,
        types.InputGroupCallStream,
        types.InputPeerPhotoFileLocation,
        types.InputPhotoFileLocation,
        types.InputPhotoLegacyFileLocation,
        types.InputSecureFileLocation,
        types.InputStickerSetThumb,
        types.InputTakeoutFileLocation
    ],
    pydantic.Field(discriminator='QUALNAME')
]
