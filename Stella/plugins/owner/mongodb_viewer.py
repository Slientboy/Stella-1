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

from Stella import OWNER_ID, StellaCli, StellaDB
from Stella.helper import custom_filter


@StellaCli.on_message(custom_filter.command('mongo'))
async def mongoViewer(client, message):
    
    if (
        message.from_user.id not in str(OWNER_ID)
    ):
        return

    if (
        len(message.command) == 1
    ):
        await message.reply(
            'Give me `MongoDB argument!`'
        )
        return

    mongo_coll = message.command[1]
    await message.reply(
        f"`{StellaDB[mongo_coll].find_one({'chat_id': message.chat.id})}`"
    )
