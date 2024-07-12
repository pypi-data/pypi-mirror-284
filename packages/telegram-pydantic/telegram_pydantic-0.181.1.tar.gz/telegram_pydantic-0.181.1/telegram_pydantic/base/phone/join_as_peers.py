from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# phone.JoinAsPeers - Layer 181
JoinAsPeers = typing.Annotated[
    typing.Union[
        types.phone.JoinAsPeers
    ],
    pydantic.Field(discriminator='QUALNAME')
]
