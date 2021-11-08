from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker_id(sticker_id = CAACAgIAAxkBAAEBSZ9hiOi5RHnnBvsUllnHX3evLOW1QgACBQADwDZPE_lqX5qCa011IgQ)
        f"""I am an Telegram Groups Music Player🎶, I let you play music in your group's voice chat.
The commands I currently support are:
`/play` - 🎶 Play the replied audio file or YouTube video 
`/pause` - ▶️ Pause the audio stream 
`/resume` - ⏸ Resume the audio stream 
`/skip` - ↪️ Skip the current audio stream
`/mute` - 🔇 Mute the user bot
`/unmute` - 🔊 Unmute the userbot
`/stop` - 🗑🛑 Clear the queue and remove the userbot from the call

Join @SDBOTsZ
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
