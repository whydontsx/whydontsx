import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ai-image"
__HELP__ = """
<blockquote><b>『 ꜱᴛᴀʟᴋɪɢ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ai-image</code> 
   <i>penjelasan:</b> untuk stalking instagram menggunakan username</i></blockquote>
"""

@PY.UBOT("ai-image")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `stalkig` followed by the Instagram username.")
    
    prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>proccesing....")
    text = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
     url = f"https://widipe.com/bingimg?text={text}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            caption = f"""
berikut
"""
            photo_path = wget.download(hasil)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
