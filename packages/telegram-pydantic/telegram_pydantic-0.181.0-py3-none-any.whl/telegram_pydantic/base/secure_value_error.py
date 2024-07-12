from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureValueError - Layer 181
SecureValueError = typing.Annotated[
    typing.Union[
        types.SecureValueError,
        types.SecureValueErrorData,
        types.SecureValueErrorFile,
        types.SecureValueErrorFiles,
        types.SecureValueErrorFrontSide,
        types.SecureValueErrorReverseSide,
        types.SecureValueErrorSelfie,
        types.SecureValueErrorTranslationFile,
        types.SecureValueErrorTranslationFiles
    ],
    pydantic.Field(discriminator='QUALNAME')
]
