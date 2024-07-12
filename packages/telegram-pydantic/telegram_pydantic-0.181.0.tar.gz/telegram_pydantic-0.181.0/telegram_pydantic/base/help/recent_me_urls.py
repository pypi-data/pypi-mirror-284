from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.RecentMeUrls - Layer 181
RecentMeUrls = typing.Annotated[
    typing.Union[
        types.help.RecentMeUrls
    ],
    pydantic.Field(discriminator='QUALNAME')
]
