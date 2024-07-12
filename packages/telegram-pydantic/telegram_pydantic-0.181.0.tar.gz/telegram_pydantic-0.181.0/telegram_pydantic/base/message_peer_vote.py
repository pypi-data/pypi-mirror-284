from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# MessagePeerVote - Layer 181
MessagePeerVote = typing.Annotated[
    typing.Union[
        types.MessagePeerVote,
        types.MessagePeerVoteInputOption,
        types.MessagePeerVoteMultiple
    ],
    pydantic.Field(discriminator='QUALNAME')
]
