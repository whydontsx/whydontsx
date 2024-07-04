from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, get_expired_date, ubot


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
🔴 pemberitahuan
akun: <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
id: {X.me.id}
reason: uꜱerbot telah habis
"""

    def START(message):
        return f"""
Selamat Datang Di Bot Saya !
Saya Adalah Bot Yang Dapat Membantu Anda Untuk Membuat Userbot
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
💬 Silahkan order terlebih dahulu

🎟️ Harga Perbulan: {harga}.000

🔖 Total Harga: rp {total}.000
🗓️ Total Bulan: {bulan} 

✅ Konfirmasi untuk melakukan pembayaran
"""

    async def UBOT(count):
        return f"""
🤖 userbot ke {int(count) + 1}/{len(ubot._ubot)}
👤 akun: <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
📍 id: {ubot._ubot[int(count)].me.id}
"""

    def POLICY():
        return """
Jika Ada Masalah Laporkan Ke Owner Saya ! @Anonymousx888
"""
