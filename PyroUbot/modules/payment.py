import asyncio
from datetime import datetime

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

CONFIRM_PAYMENT = []


@PY.CALLBACK("^confirm")
async def _(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    CONFIRM_PAYMENT.append(get.id)
    try:
        await callback_query.message.delete()
        pesan = await bot.ask(
            user_id,
            f"""
silahkan melakukan pembayaran            

QRIS : https://telegra.ph//file/a673c21de9f6ff1c50d2d.jpg
""",
            timeout=300,
        )
    except asyncio.TimeoutError as out:
        return await bot.send_message(get.id, "pembatalan otomatis")
    if get.id in CONFIRM_PAYMENT:
        if not pesan.photo:
            CONFIRM_PAYMENT.remove(get.id)
            buttons = [[InlineKeyboardButton("✅ konfirmasi", callback_data="confirm")]]
            return await bot.send_message(
                user_id,
                """
tidak dapat diproses

harap kirimkan screenshot bukti pembayaran anda yang valid

silahkan konfirmasi ulang pembayaran anda
""",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        elif pesan.photo:
            buttons = BTN.ADD_EXP(get.id)
            await pesan.copy(
                OWNER_ID,
                reply_markup=buttons,
            )
            CONFIRM_PAYMENT.remove(get.id)
            buttons = [
                [InlineKeyboardButton("owner", url="https://t.me/anonymousx888")]
            ]
            return await bot.send_message(
                user_id,
                f"""
baik {full_name} silahkan ditunggu dan jangan spam ya
pembayaran anda akan dikonfirmasi setelah 1-12 jam kerja
jika pembayaran anda belum di konfirmasi silahkan hubungi admin
""",
                reply_markup=InlineKeyboardMarkup(buttons),
            )


@PY.CALLBACK("^(kurang|tambah)")
async def _(client, callback_query):
    BULAN = int(callback_query.data.split()[1])
    HARGA = 30
    QUERY = callback_query.data.split()[0]
    try:
        if QUERY == "kurang":
            if BULAN > 1:
                BULAN -= 1
                TOTAL_HARGA = HARGA * BULAN
        elif QUERY == "tambah":
            if BULAN < 12:
                BULAN += 1
                TOTAL_HARGA = HARGA * BULAN
        buttons = BTN.PLUS_MINUS(BULAN, callback_query.from_user.id)
        await callback_query.message.edit_text(
            MSG.TEXT_PAYMENT(HARGA, TOTAL_HARGA, BULAN),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except:
        pass


@PY.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    query = callback_query.data.split()
    get_user = await bot.get_users(query[1])
    if query[0] == "success":
        buttons = [
            [InlineKeyboardButton("⚒️ buat userbot ⚒️", callback_data="buat_ubot")],
        ]
        await bot.send_message(
            get_user.id,
            f"""
pembayaran anda berhasil dikonfirmasi
sekarang anda bisa membuat userbot
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await add_to_vars(client.me.id, "PREM_USERS", get_user.id)
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(query[2]))
        await set_expired_date(get_user.id, expired)
        return await callback_query.edit_message_text(
            f"""
✅ {get_user.first_name} {get_user.last_name or ''} ditambahkan ke anggota premium
""",
        )
    if query[0] == "failed":
        buttons = [
            [
                InlineKeyboardButton(
                    "💳 lakukan pembayaran 💳", callback_data="bayar_dulu"
                )
            ],
        ]
        await bot.send_message(
            get_user.id,
            """
❌ pembayaran anda tidak bisa dikonfirmasi

💬 silahkan lakukan pembayaran dengan benar
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return await callback_query.edit_message_text(
            f"""
❌ {get_user.first_name} {get_user.last_name or ''} tidak ditambahkan ke anggota premium
""",
        )
    if query[0] == "home":
        if get_user.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get_user.id)
            buttons_home = BTN.START(callback_query)
            return await callback_query.edit_message_text(
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons_home),
            )
        else:
            buttons_home = BTN.START(callback_query)
            return await callback_query.edit_message_text(
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons_home),
            )
