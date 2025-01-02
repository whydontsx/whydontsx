import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.types import ChatPermissions
from PyroUbot import *


__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = """
<blockquote>Bantuan Untuk Global

perintah : <code>{0}gban</code>
    banned user dari semua group chat 

perintah : <code>{0}ungban</code>
    unbanned user dari semua group chat

perintah : <code>{0}gmute</code>
    untuk mengemute user dari semua gc yg kmu admin 

perintah : <code>{0}ungmute</code>
    untuk meng ungmute user dari semua gc yg kmu admin</blockquote> 
"""

      
@py.ubot("gban")
@py.devs("cgban")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(cgr("glbl_3").format(em.gagal))
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(cgr("glbl_4").format(em.gagal))
        return
    if m.reply_to_message:
        alasan = m.text.split(None, 1)[1]
    else:
        alasan = m.text.split(None, 2)[2]
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog(c, "gban")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if dbgb.check_gban(nyet):
            await xx.edit(cgr("glbl_5").format(em.gagal))
            return
        try:
            await c.ban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
            await c.ban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
    dbgb.add_gban(nyet, alasan, c.me.id)
    await c.block_user(nyet)
    await nlx.invoke(
        DeleteHistory(peer=(await nlx.resolve_peer(nyet)), max_id=0, revoke=True)
    )
    mmg = cgr("glbl_6").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await m.reply(mmg)
    await xx.delete()


@py.ubot("ungban")
@py.devs("cungban")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    await c.get_users(nyet)
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog(c, "gban")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if not dbgb.check_gban(nyet):
            await xx.edit(cgr("glbl_7").format(em.gagal))
            return
        try:
            await c.unban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dbgb.remove_gban(nyet)
    await c.unblock_user(nyet)
    mmg = cgr("glbl_8").format(em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention)
    await m.reply(mmg)
    await xx.delete()


@py.ubot("gmute")
@py.devs("cgmute")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(cgr("glbl_3").format(em.gagal))
        return
    if len(m.text.split()) == 2 and not m.reply_to_message:
        await xx.edit(cgr("glbl_9").format(em.gagal))
        return
    if m.reply_to_message:
        alasan = m.text.split(None, 1)[1]
    else:
        alasan = m.text.split(None, 2)[2]
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog(c, "grup")

    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if dbgm.check_gmute(nyet):
            await xx.edit(cgr("glbl_10").format(em.gagal))
            return
        try:
            await c.restrict_chat_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.add_gmute(nyet, alasan, c.me.id)
    mmg = cgr("glbl_11").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await m.reply(mmg)
    await xx.delete()


@py.ubot("ungmute")
@py.devs("cungmute")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    nyet, _ = await c.extract_user_and_reason(m)
    xx = await m.reply(cgr("proses").format(em.proses))
    await c.get_users(nyet)
    if len(m.text.split()) == 1:
        await xx.edit(cgr("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog(c, "grup")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    for chat in chats:
        if not dbgm.check_gmute(nyet):
            await xx.edit(cgr("glbl_12").format(em.gagal))
            return
        try:
            await c.unban_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dbgm.remove_gmute(nyet)
    mmg = cgr("glbl_13").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention
    )
    await m.reply(mmg)
    await xx.delete()


@py.ubot("gbanlist|listgban")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    gbanu = dbgb.load_from_db()
    msg = await m.reply(cgr("proses").format(em.proses))

    if not gbanu:
        return await msg.edit(cgr("glbl_22").format(em.gagal))
    dftr = cgr("glbl_14").format(em.profil)
    for ii in gbanu:
        dftr += cgr("glbl_15").format(em.block, ii["_id"])
        if ii["reason"]:
            dftr += cgr("glbl_16").format(
                em.warn, ii["reason"], em.sukses, dbgb.count_gbans()
            )
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gbanlist.txt"
            await m.reply_document(document=f, caption=cgr("glbl_17").format(em.profil))
    await msg.delete()
    return


@py.ubot("gmutelist|listgmute")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    gmnu = dbgm.load_from_db()
    msg = await m.reply(cgr("proses").format(em.proses))
    if not gmnu:
        await msg.edit(cgr("glbl_2").format(em.gagal))
        return
    dftr = cgr("glbl_18").format(em.profil)
    for ii in gmnu:
        dftr += cgr("glbl_19").format(em.warn, ii["_id"])
        if ii["reason"]:
            dftr += cgr("glbl_20").format(
                em.warn, ii["reason"], em.sukses, dbgm.count_gmutes()
            )
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gmutelist.txt"
            await m.reply_document(document=f, caption=cgr("glbl_21").format(em.profil))
    await msg.delete()
    return
