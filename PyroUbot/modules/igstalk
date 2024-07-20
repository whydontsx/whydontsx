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
                    result = data['result']
                    username = result.get('username', 'N/A')
                    fullName = result.get('fullName', 'N/A')
                    bio = result.get('bio', 'N/A')
                    posts = result.get('posts', 'N/A')
                    followers = result.get('followers', 'N/A')
                    following = result.get('following', 'N/A')
                    postsCount = result.get('postsCount', 'N/A')
                    photoUrl = result.get('photoUrl', 'N/A')

                    await prs.edit(
                        f"""
╭─ •  「 Instagram Stalk 」
│  ◦  Username : {username}
│  ◦  Nickname : {fullName}
│  ◦  Followers : {followers}
│  ◦  Following : {following}
│  ◦  Posting : {postsCount}
│  ◦  Link : https://instagram.com/{username}
│  ◦  Bio : {bio}
│  ◦  Photo : {photoUrl}
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
