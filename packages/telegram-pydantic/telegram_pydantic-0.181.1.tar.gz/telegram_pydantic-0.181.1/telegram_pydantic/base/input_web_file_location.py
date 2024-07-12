from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputWebFileLocation - Layer 181
InputWebFileLocation = typing.Annotated[
    typing.Union[
        types.InputWebFileAudioAlbumThumbLocation,
        types.InputWebFileGeoPointLocation,
        types.InputWebFileLocation
    ],
    pydantic.Field(discriminator='QUALNAME')
]
