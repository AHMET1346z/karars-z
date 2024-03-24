from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["aktifses"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("➻ 𝖠𝗄𝗍𝗂𝖿 𝗌𝖾𝗌 𝗒𝗎̈𝗄𝗅𝖾𝗇𝗂𝗒𝗈𝗋 ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"➻ 𝖠𝗄𝗍𝗂𝖿 𝗌𝖾𝗌 𝖻𝗎𝗅𝗎𝗇𝖺𝗆𝖺𝖽ı {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>➻ 𝖠𝗄𝗍𝗂𝖿 𝗌𝖾𝗌 𝗌𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝗂 :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["aktifvideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("➻ 𝖠𝗄𝗍𝗂𝖿 𝗏𝗂𝖽𝖾𝗈 𝗒𝗎̈𝗄𝗅𝖾𝗇𝗂𝗒𝗈𝗋 ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"➻ 𝖠𝗄𝗍𝗂𝖿 𝗏𝗂𝖽𝖾𝗈 𝖻𝗎𝗅𝗎𝗇𝖺𝗆𝖺𝖽ı {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>➻ 𝖠𝗄𝗍𝗂𝖿 𝗏𝗂𝖽𝖾𝗈 𝗌𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝗂 :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
