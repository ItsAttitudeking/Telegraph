from pyrogram import Client, filters
import os, shutil
from creds import my
from telegraph import upload_file
import logging

logging.basicConfig(level=logging.INFO)


TGraph = Client(
    "Image upload bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH
)


@TGraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"<b>Hello {message.from_user.first_name}, My Name Is TELEGRAPH MAKER 🥳\n\nI'm A <u>𝗧𝗘𝗟𝗚𝗥𝗔𝗣𝗛 𝗨𝗣𝗟𝗢𝗔𝗗𝗘𝗥 𝗥𝗢𝗕𝗢𝗧.</u>\n\nSend Me Any 𝗚𝗜𝗙, 𝗜𝗠𝗔𝗚𝗘𝗦 & 𝗠𝗣𝟰 𝗩𝗜𝗗𝗘𝗢 & I'll Upload It On Telegra.ph & Send You Back A Link\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @Modzilla 𝗜𝗳 𝗬𝗼𝘂 𝗟𝗼𝘃𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 ♥️.</b>", True)
    
@TGraph.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("downloads",str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    imgdir = tmp + "/" + str(message.message_id) +".jpg"
    dwn = await message.reply_text("Downloading...", True)          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("Uploading...")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp,ignore_errors=True)


TGraph.run()
