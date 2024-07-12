from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# auth.SentCodeType - Layer 181
SentCodeType = typing.Annotated[
    typing.Union[
        types.auth.SentCodeTypeApp,
        types.auth.SentCodeTypeCall,
        types.auth.SentCodeTypeEmailCode,
        types.auth.SentCodeTypeFirebaseSms,
        types.auth.SentCodeTypeFlashCall,
        types.auth.SentCodeTypeFragmentSms,
        types.auth.SentCodeTypeMissedCall,
        types.auth.SentCodeTypeSetUpEmailRequired,
        types.auth.SentCodeTypeSms,
        types.auth.SentCodeTypeSmsPhrase,
        types.auth.SentCodeTypeSmsWord
    ],
    pydantic.Field(discriminator='QUALNAME')
]
