from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.WallPapers - Layer 181
WallPapers = typing.Annotated[
    typing.Union[
        types.account.WallPapers,
        types.account.WallPapersNotModified
    ],
    pydantic.Field(discriminator='QUALNAME')
]
