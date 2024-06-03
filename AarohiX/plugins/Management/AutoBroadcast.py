import asyncio
import datetime
from AarohiX import app
from pyrogram import Client
from AarohiX.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://graph.org/file/84c0de2a54bf34e2a8de6.jpg+"


MESSAGE = f"""
● ʜᴇʏ, ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ\n\n● ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ ᴇɴᴊᴏʏ... ɴᴏ ʟᴀɢ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ\n● ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ ᴀɴᴅ ʟᴀɢ ꜰʀᴇᴇ ᴍᴜꜱɪᴄ 🎶\n❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ."

💞ᴊᴏɪɴ » [✘ ᴄʟɪᴄᴋ ᴍᴇ ✘](https://t.me/ll_stylish_dpz_ll) <√ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ ɢʀᴏᴜᴘ.^>

🚩 ʙᴏᴛ »|| @{app.username}||"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("» ᴀᴅᴅ ᴍᴇ «", url=f"https://t.me/Queen_of_heart_music_bot?startgroup=true")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())
