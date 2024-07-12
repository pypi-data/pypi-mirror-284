from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# account.PrivacyRules - Layer 181
PrivacyRules = typing.Annotated[
    typing.Union[
        types.account.PrivacyRules
    ],
    pydantic.Field(discriminator='QUALNAME')
]
