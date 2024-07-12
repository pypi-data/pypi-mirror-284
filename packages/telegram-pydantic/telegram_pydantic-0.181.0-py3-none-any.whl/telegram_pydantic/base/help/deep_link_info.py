from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# help.DeepLinkInfo - Layer 181
DeepLinkInfo = typing.Annotated[
    typing.Union[
        types.help.DeepLinkInfo,
        types.help.DeepLinkInfoEmpty
    ],
    pydantic.Field(discriminator='QUALNAME')
]
