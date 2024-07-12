from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types

# ChannelAdminLogEventAction - Layer 181
ChannelAdminLogEventAction = typing.Annotated[
    typing.Union[
        types.ChannelAdminLogEventActionChangeAbout,
        types.ChannelAdminLogEventActionChangeAvailableReactions,
        types.ChannelAdminLogEventActionChangeEmojiStatus,
        types.ChannelAdminLogEventActionChangeEmojiStickerSet,
        types.ChannelAdminLogEventActionChangeHistoryTTL,
        types.ChannelAdminLogEventActionChangeLinkedChat,
        types.ChannelAdminLogEventActionChangeLocation,
        types.ChannelAdminLogEventActionChangePeerColor,
        types.ChannelAdminLogEventActionChangePhoto,
        types.ChannelAdminLogEventActionChangeProfilePeerColor,
        types.ChannelAdminLogEventActionChangeStickerSet,
        types.ChannelAdminLogEventActionChangeTitle,
        types.ChannelAdminLogEventActionChangeUsername,
        types.ChannelAdminLogEventActionChangeUsernames,
        types.ChannelAdminLogEventActionChangeWallpaper,
        types.ChannelAdminLogEventActionCreateTopic,
        types.ChannelAdminLogEventActionDefaultBannedRights,
        types.ChannelAdminLogEventActionDeleteMessage,
        types.ChannelAdminLogEventActionDeleteTopic,
        types.ChannelAdminLogEventActionDiscardGroupCall,
        types.ChannelAdminLogEventActionEditMessage,
        types.ChannelAdminLogEventActionEditTopic,
        types.ChannelAdminLogEventActionExportedInviteDelete,
        types.ChannelAdminLogEventActionExportedInviteEdit,
        types.ChannelAdminLogEventActionExportedInviteRevoke,
        types.ChannelAdminLogEventActionParticipantInvite,
        types.ChannelAdminLogEventActionParticipantJoin,
        types.ChannelAdminLogEventActionParticipantJoinByInvite,
        types.ChannelAdminLogEventActionParticipantJoinByRequest,
        types.ChannelAdminLogEventActionParticipantLeave,
        types.ChannelAdminLogEventActionParticipantMute,
        types.ChannelAdminLogEventActionParticipantToggleAdmin,
        types.ChannelAdminLogEventActionParticipantToggleBan,
        types.ChannelAdminLogEventActionParticipantUnmute,
        types.ChannelAdminLogEventActionParticipantVolume,
        types.ChannelAdminLogEventActionPinTopic,
        types.ChannelAdminLogEventActionSendMessage,
        types.ChannelAdminLogEventActionStartGroupCall,
        types.ChannelAdminLogEventActionStopPoll,
        types.ChannelAdminLogEventActionToggleAntiSpam,
        types.ChannelAdminLogEventActionToggleForum,
        types.ChannelAdminLogEventActionToggleGroupCallSetting,
        types.ChannelAdminLogEventActionToggleInvites,
        types.ChannelAdminLogEventActionToggleNoForwards,
        types.ChannelAdminLogEventActionTogglePreHistoryHidden,
        types.ChannelAdminLogEventActionToggleSignatures,
        types.ChannelAdminLogEventActionToggleSlowMode,
        types.ChannelAdminLogEventActionUpdatePinned
    ],
    pydantic.Field(discriminator='QUALNAME')
]
