from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ReactionNotificationsFrom - Layer 181
ReactionNotificationsFrom = typing.Annotated[
    typing.Union[
        types.ReactionNotificationsFromAll,
        types.ReactionNotificationsFromContacts
    ],
    pydantic.Field(discriminator='QUALNAME')
]
