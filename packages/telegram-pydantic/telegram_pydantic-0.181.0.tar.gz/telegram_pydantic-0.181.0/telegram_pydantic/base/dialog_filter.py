from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# DialogFilter - Layer 181
DialogFilter = typing.Annotated[
    typing.Union[
        types.DialogFilter,
        types.DialogFilterChatlist,
        types.DialogFilterDefault
    ],
    pydantic.Field(discriminator='QUALNAME')
]
