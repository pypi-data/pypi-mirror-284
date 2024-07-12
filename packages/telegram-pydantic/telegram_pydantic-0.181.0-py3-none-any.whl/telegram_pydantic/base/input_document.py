from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputDocument - Layer 181
InputDocument = typing.Annotated[
    typing.Union[
        types.InputDocument,
        types.InputDocumentEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
