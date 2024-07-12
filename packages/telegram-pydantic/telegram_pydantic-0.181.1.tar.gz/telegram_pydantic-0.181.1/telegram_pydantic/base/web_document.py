from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# WebDocument - Layer 181
WebDocument = typing.Annotated[
    typing.Union[
        types.WebDocument,
        types.WebDocumentNoProxy
    ],
    pydantic.Field(discriminator='QUALNAME')
]
