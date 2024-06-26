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

from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=['purge', 'spurge']))
async def purge(client, message):
    message_id = message.id + 1
    chat_id = message.chat.id
    command = message.command[0]
    MessageIDs = []

    if command == 'purge':
        LastMessageDelete = False
    elif command == 'spurge':
        LastMessageDelete = True

    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return

    if not message.reply_to_message:
        await message.reply(
            'Reply to a message to show me where to purge from.'
        )
        return
        
    reply_to_message = message.reply_to_message.id
    for messageID in range(reply_to_message, message_id):
        MessageIDs.append(messageID)
    
    try:
        await StellaCli.delete_messages(
            chat_id=chat_id,
            message_ids=MessageIDs
        )

        if not LastMessageDelete:
            await StellaCli.send_message(
                chat_id=chat_id,
                text="Purge completed!"
            )
    except:
        await message.reply(
            "I can't delete messages here! Make sure I'm admin and can delete other user's messages."
        )

