from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# messages.VotesList - Layer 181
VotesList = typing.Annotated[
    typing.Union[
        types.messages.VotesList
    ],
    pydantic.Field(discriminator='QUALNAME')
]
