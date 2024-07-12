from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.SponsoredMessages - Layer 181
SponsoredMessages = typing.Annotated[
    typing.Union[
        types.messages.SponsoredMessages,
        types.messages.SponsoredMessagesEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
