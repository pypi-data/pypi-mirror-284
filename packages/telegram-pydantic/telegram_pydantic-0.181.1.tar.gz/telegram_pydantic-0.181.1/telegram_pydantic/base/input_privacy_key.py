from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# InputPrivacyKey - Layer 181
InputPrivacyKey = typing.Annotated[
    typing.Union[
        types.InputPrivacyKeyAbout,
        types.InputPrivacyKeyAddedByPhone,
        types.InputPrivacyKeyBirthday,
        types.InputPrivacyKeyChatInvite,
        types.InputPrivacyKeyForwards,
        types.InputPrivacyKeyPhoneCall,
        types.InputPrivacyKeyPhoneNumber,
        types.InputPrivacyKeyPhoneP2P,
        types.InputPrivacyKeyProfilePhoto,
        types.InputPrivacyKeyStatusTimestamp,
        types.InputPrivacyKeyVoiceMessages
    ],
    pydantic.Field(discriminator='QUALNAME')
]
