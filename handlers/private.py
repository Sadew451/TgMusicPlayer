from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgQAAx0CQ2C8OgACsqNhiisoWUQROohUrpaGzDsHsot3dQACVxYAAtqjlSznBlAxygdMwyIE"


START_TEXT = """
👋 Hey {} I am an Telegram Groups Music Player, I let you play music in your group's voice chat.

**Commands** [Here](telegra.ph/A-Simple-Group-Music-player-bot-by-SDBotsz-11-09-2)

Join @SDBotsz. 🔥
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url="https://t.me/SDBOTs_inifinity"),
        InlineKeyboardButton('Group', url='https://t.me/SDBOTz')
        InlineKeyboardButton('Group', url='https://t.me/SDBOTz')
        ]]
  
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_sticker(STICKER)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )

