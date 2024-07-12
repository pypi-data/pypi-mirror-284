from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.InviteText - Layer 181
InviteText = typing.Annotated[
    typing.Union[
        types.help.InviteText
    ],
    pydantic.Field(discriminator='QUALNAME')
]
