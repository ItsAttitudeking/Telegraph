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
    await message.reply_text(f"<b>Hello {message.from_user.first_name}, [π](https://telegra.ph/file/bb9126bc70e63a4121234.jpg)My Name Is TELEGRAPH MAKER π₯³\n\nI'm A <u>π§ππππ₯ππ£π π¨π£ππ’ππππ₯ π₯π’ππ’π§.</u>\n\nποΈSend Me Any πππ, ππ ππππ¦ & π π£π° π©ππππ’ & I'll Upload It On Telegra.ph & Send You Back A Link\n\nποΈπ¦ππ―ππ°πΏπΆπ―π² @Attitude_Network\n\nπ°ππ³ π¬πΌπ ππΌππ² π§π΅πΆπ ππΌπ β₯οΈ.</b>", True)
    
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
    await dwn.edit_text(f"πLink: https://telegra.ph{response[0]} \n\n\n πππ¨π°ππ«ππ ππ² : @Attitude_Network")
    shutil.rmtree(tmp,ignore_errors=True)


TGraph.run()
