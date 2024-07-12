from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessagePeerReaction - Layer 181
MessagePeerReaction = typing.Annotated[
    typing.Union[
        types.MessagePeerReaction
    ],
    pydantic.Field(discriminator='QUALNAME')
]
