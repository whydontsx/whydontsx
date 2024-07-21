import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "stalkff"
__HELP__ = """
<b>『 stalkff 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stalkff</code> 
   <i>penjelasan:</b> search akun ff menggunakan id</i>
"""

@PY.UBOT("stalkff")
async def stalkff(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `stalkff` id akun.")
    
    lyrics = message.command[1]
    chat_id = message.chat.id
    url = f"https://ff.lxonfire.workers.dev/?id={lyrics}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            lyrics = data['region']
            photoUrl = data['img_url']
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>{lyrics}</b>
"""
            photo_path = wget.download(photoUrl)
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
