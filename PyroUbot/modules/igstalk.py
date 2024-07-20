from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message


@PY.UBOT("stalkig")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : ask bagaimana membuat donat?"
            )
        else:
            prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji>proccesing....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/stalk/ig?username={a}&apikey=ApiKhususWannAza')

            if response.status_code == 200:
                data = response.json()
                if 'result' in data:
                    username = data['result']['username']['fullName']['bio']['posts']['followers']['following']['postsCount']['photoUrl']
                    await prs.edit(
                        f"""
╭─ •  「 Instagram Stalk 」
│  ◦  Username : ${username}
│  ◦  Nickname : ${fullName}
│  ◦  Followers : ${followers}
│  ◦  Following : ${following}
│  ◦  Posting : ${postsCount}
│  ◦  Link : https://instagram.com/${username}
│  ◦  Bio : ${bio}
╰──── •
"""
                    )
                else:
                    await message.reply_text("No 'result' key found in the response.")
            else:
                await message.reply_text("Failed to get a valid response from the API.")
    except KeyError:
        await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
