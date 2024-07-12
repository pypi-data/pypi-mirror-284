from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# SecureSecretSettings - Layer 181
SecureSecretSettings = typing.Annotated[
    typing.Union[
        types.SecureSecretSettings
    ],
    pydantic.Field(discriminator='QUALNAME')
]
