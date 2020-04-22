from telegram import ChatAction
import html
import urllib.request
import re
import json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from tg_bot import dispatcher
from tg_bot.__main__ import STATS, USER_INFO
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import bot_admin, user_admin, is_user_ban_protected, can_restrict, \
    is_user_admin, is_user_in_chat, is_bot_admin
    
@bot_admin
@user_admin
def butts(bot: Bot, update: Update, args: List[str]) -> str:
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    final = "http://media.obutts.ru/{}".format(nsfw)
    update.message.reply_photo(final)
		
__help__ = """
 - /boobs: Sends Random Boobs pic.
 - /butts: Sends Random Butts pic.
"""
__mod_name__ = "NSFW"
BUTTS_HANDLER = DisableAbleCommandHandler("butts", butts, pass_args=True, filters=Filters.group, admin_ok=True)
dispatcher.add_handler(BUTTS_HANDLER)
