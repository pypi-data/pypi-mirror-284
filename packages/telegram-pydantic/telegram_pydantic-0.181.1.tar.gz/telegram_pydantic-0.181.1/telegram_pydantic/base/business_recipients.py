from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessRecipients - Layer 181
BusinessRecipients = typing.Annotated[
    typing.Union[
        types.BusinessRecipients
    ],
    pydantic.Field(discriminator='QUALNAME')
]
