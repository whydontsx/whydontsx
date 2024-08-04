from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!

<b>💬 @{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ</b>

🚀 ꜱɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ 
• ᴏᴡɴᴇʀ : <a href=tg://openmessage?user_id={OWNER_ID}>ᴡᴀɴɴꜰʏʏ</a> 

ʟɪsᴛ ʜᴀʀɢᴀ & ᴋᴇʙᴜᴛᴜʜᴀɴ ᴜsᴇʀʙᴏᴛ :
<a href='https://t.me/TestiByWann/3526'>ᴋᴇʙᴜᴛᴜʜᴀɴ ᴜsᴇʀʙᴏᴛ</a>

👉🏻 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ</b></blockquote>
"""

    def TEXT_PAYMENT(HARGA, TOTAL_HARGA, BULAN):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: 15.000</b>

<b>💳 ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ ʙᴀɴᴋ ᴊᴀɢᴏ : `103177506039` <b>RAH**H</b> </b>
 <b>├ ᴅᴀɴᴀ : `085366293093` <b>RAH**H</b> </b>
 <b>├ ɢᴏᴘᴀʏ : `085366293093` <b>RAH**H</b> </b>
 <b>├ ǫʀɪs : TANYAKAN SAJA</b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ 15.000 ᴘᴇʀʙᴜʟᴀɴ</b> 

 🚀 ꜱɪʟᴀʜᴋᴀɴ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ 
• ᴏᴡɴᴇʀ : <a href=tg://openmessage?user_id={OWNER_ID}>ᴡᴀɴɴꜰʏʏ</a> 

<b>✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>❏ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """
ᴊɪᴋᴀ ᴀᴅᴀ ᴍᴀꜱᴀʟᴀʜ ʟᴀᴘᴏʀᴋᴀɴ ᴋᴇ ᴏᴡɴᴇʀ ꜱᴀʏᴀ ! @wannoffc08
"""
