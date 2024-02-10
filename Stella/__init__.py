
"""

[telegram]
api_id = "2568615"
api_hash = "1e62cca9207a4469ca847526acebb660"

[tekegram.bot]
bot_token = "6956874781:AAGzsdSn3rSahmDx5hxlu9N6SvEFycubg_8"
name = "Elaina"
username = "@Elaina"
user_id = "2069340770"

[database]
database_url = "mongodb+srv://elianaapi:pranav8935@cluster0.gf5ky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

[settings]
owner = "1194169408"
sudo_users = ['1194169408']

[settings.commands]
prefix = ['!', '/']

[settings.log]
chat_id = "-1001251337410"

[settings.backup]
chat_id = "-1001251337410"

[api.stella]
api_key = ""
"""

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

import sys

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
from pyrogram import Client
from pyromod import listen

#from Stella.config import Config
from Stella.StellaGban import StellaClient

#from stellagban import StellaClient


APP_ID = "2568615"
API_HASH = "1e62cca9207a4469ca847526acebb660"
OWNER_ID = "1194169408"
BOT_TOKEN = "6956874781:AAGzsdSn3rSahmDx5hxlu9N6SvEFycubg_8"
BOT_ID = "2069340770"
BOT_NAME = "stella"
BOT_USERNAME = "@missstella"
LOG_CHANNEL = "-1001251337410"
SUDO_USERS = None
PREFIX = ['!', '/']
DATABASE_URI = "mongodb+srv://elianaapi:pranav8935@cluster0.gf5ky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
BACKUP_CHAT = "-1001251337410"
StellaGbanAPI = None
session_name = BOT_TOKEN.split(":")[0]

StellaCli = Client(
    session_name,
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


StellaAPI = StellaClient(api_key=StellaGbanAPI)

scheduler = AsyncIOScheduler()

try:
    StellaMongoClient = MongoClient(DATABASE_URI)
    StellaDB = StellaMongoClient.stella_mongo
except:
    sys.exit(f"{BOT_NAME}'s database is not running!")

TELEGRAM_SERVICES_IDs = (
    [
        777000, # Telegram Service Notifications
        1087968824 # GroupAnonymousBot
    ]
)

GROUP_ANONYMOUS_BOT = 1087968824
