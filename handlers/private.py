from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgQAAx0CQ2C8OgACsqNhiisoWUQROohUrpaGzDsHsot3dQACVxYAAtqjlSznBlAxygdMwyIE"

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(STICKER)
    await message.reply_text(
        f"""👋 Hey [{}](tg://user?id={}), I am an Telegram Groups Music Player, I let you play music in your group's voice chat.

**Commands** [Here](telegra.ph/A-Simple-Group-Music-player-bot-by-SDBotsz-11-09-2)

Join @SDBotsz. 🔥
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel 🙋‍♀️", url="https://t.me/SDBOTs_inifinity"
                    ),
                    InlineKeyboardButton(
                        "Developer 👩‍💻", url="https://t.me/Itz_Sadew"
                    )
                ]
            ]
        )
    )
