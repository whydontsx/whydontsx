from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ǫᴜᴏᴛᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ quotes 』</b>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}quotes [query]</code>

<b>Query:</b> <b>anime</b>,
    <b>bucin</b>,
    <b>dilan</b>,
    <b>galau</b>,
    <b>gombal</b>,
    <b>islami</b>,
    <b>jawa</b></blockquote>
"""

URLS = {
    "anime": "https://api.junn4.my.id/quotes/anime",
    "bucin": "https://api.junn4.my.id/quotes/bucin",
    "dilan": "https://api.junn4.my.id/quotes/dilan",
    "galau": "https://api.junn4.my.id/quotes/galau",
    "gombal": "https://api.junn4.my.id/quotes/gombal",
    "islami": "https://api.junn4.my.id/quotes/islami",
    "jawa": "https://api.junn4.my.id/quotes/jawa"
}

@PY.UBOT("quotes")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar cecan Error: {e}")
