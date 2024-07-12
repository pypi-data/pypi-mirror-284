from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# BusinessBotRecipients - Layer 181
BusinessBotRecipients = typing.Annotated[
    typing.Union[
        types.BusinessBotRecipients
    ],
    pydantic.Field(discriminator='QUALNAME')
]
