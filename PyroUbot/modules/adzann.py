import json

import requests
from PyroUbot import *

__MODULE__ = "Adzan"
__HELP__ = f"""
Bantuan Untuk Adzan


• Perintah: <code>.adzan</code> [nama kota]
• Penjelasan: Untuk mengetahui jadwal adzan di lokasi anda.


© {bot.me.first_name.split()[0]}
"""


@PY.UBOT("adzan")
async def _(client, message):
    if len(message.text.split()) < 2:
        await message.reply_text("<blockquote><b>Silahkan Masukkan Nama Kota Anda</b></blockquote>")
        return
    LOKASI = message.text.split()[1]
    try:
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await message.reply_text("<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit:</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh:</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar:</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib:</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya:</b> <code>{result['items'][0]['isha']}</code>
"""
    await message.reply_text(message, catresult)
