from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.CodeType - Layer 181
CodeType = typing.Annotated[
    typing.Union[
        types.auth.CodeTypeCall,
        types.auth.CodeTypeFlashCall,
        types.auth.CodeTypeFragmentSms,
        types.auth.CodeTypeMissedCall,
        types.auth.CodeTypeSms
    ],
    pydantic.Field(discriminator='QUALNAME')
]
