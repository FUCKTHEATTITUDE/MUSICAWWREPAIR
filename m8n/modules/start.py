import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from m8n.utils.filters import command

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import BOT_NAME



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""Hello 👋 My name is **{BOT_NAME}**
        I'm a telegram streaming bot with some useful features. Supporting platforms like Youtube, Spotify, Resso, AppleMusic , Soundcloud etc.

Feel free to add me to your groups.""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏳‍🌈 About", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "☁️ Others", callback_data="others")
                ],
                [
                    InlineKeyboardButton(
                        "🗂 Commands", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Click here to Summon Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def gcstart(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"Thanks for adding me in your group !! If you want to use me with right actions promote me as admin in this Chat.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Bot Owner", url=f"https://t.me/{OWNER_USERNAME}")
                ]
            ]
        ),
    )
