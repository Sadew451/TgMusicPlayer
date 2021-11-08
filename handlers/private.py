from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(sticker = "CAACAgUAAxkBAAEBN9FhhMQq99NL0eY70r47LmPghi9fsQAC2QUAAss5KFT5r0lsTegDZiIE")
          await message.reply_text(text =f"👋 Hello **{message.from_user.first_name }**. \n\nI am simple Google Translater Bot.**I can translate any language to you selected language** My Dear **`{message.from_user.first_name }`**  __\n\n**Powerd By** @SDbotsz. 🔥",
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
