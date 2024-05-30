from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from AnonXMusic import app
from MukeshAPI import api
from pyrogram.enums import ChatAction,ParseMode

@app.on_message(filters.command("draw"))
async def draw_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    mukesh=await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    try:
        await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("mukesh.jpg", 'wb') as f:
            f.write(x)
        caption = f"""
    💘sᴜᴄᴇssғᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ : {text}
    ✨ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ : @{BOT_USERNAME}
    🥀ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
    """
        await mukesh.delete()
        await message.reply_photo("mukesh.jpg",caption=caption,quote=True)
    except Exception as e:
        await mukesh.edit_text(f"error {e}")
