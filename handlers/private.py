from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgUAAxkBAAEBSiphiQvgoSco_PZ69hZOb6LmHi7y5wACrgUAAqcESVQjjAq485SvXyIE"

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(STICKER)
    await message.reply_text(
        f"""👋 Hey **{message.from_user.first_name }**, I am an Telegram Groups Music Player, I let you play music in your group's voice chat.

`/play` - Play the replied audio file or YouTube video
`/pause` -  Pause the audio stream
`/resume` - Resume the audio stream
`/skip` -  Skip the current audio stream
`/mute` - Mute the user bot
`/unmute` - Unmute the userbot
`/stop` - Clear the queue and remove the userbot from the call

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
                     
                    InlineKeyboardButton(
                        "Developer 👩‍💻", url="https://t.me/Itz_Sadew"
                    )
                ]
            ]
        )
    )
