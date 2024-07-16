#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import asyncio, time
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from config import FSUB_UPDATES, FSUB_GROUP, SUNRISES_PIC

START_TEXT = """
Hᴇʟʟᴏ Mᴀᴡа❤️! I ᴀᴍ ᴛʜᴇ Mediainfo 𝟸𝟺 Bᴏᴛ⚡

Mᴀᴅᴇ ʙʏ <b><a href=https://t.me/Sunrises24botupdates>SUNRISES ™💥</a></b> ᴀɴᴅ <b><a href=https://t.me/Sunrises_24>Sᴜɴʀɪꜱᴇꜱ Hᴀʀꜱʜᴀ 𝟸𝟺❤️</a></b>.

#SUNRISES24BOTS #SIMPLERENAME24BOT
"""

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
 
joined_channel_1 = {}
joined_channel_2 = {}

@Client.on_message(filters.command("start"))
async def start(bot, msg: Message):
    user_id = msg.chat.id
    
    # Check for channel 1 (updates channel) membership
    if FSUB_UPDATES:
        try:
            user = await bot.get_chat_member(FSUB_UPDATES, user_id)
            if user.status == "kicked":
                await msg.reply_text("Sorry, you are **banned**.")
                return
        except UserNotParticipant:
            await msg.reply_text(
                text="**Please join my first updates channel before using me.**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="Join Updates Channel", url=f"https://t.me/{FSUB_UPDATES}")]
                ])
            )
            joined_channel_1[user_id] = False
            return
        else:
            joined_channel_1[user_id] = True

    # Check for channel 2 (group) membership
    if FSUB_GROUP:
        try:
            user = await bot.get_chat_member(FSUB_GROUP, user_id)
            if user.status == "kicked":
                await msg.reply_text("Sorry, you are **banned**.")
                return
        except UserNotParticipant:
            await msg.reply_text(
                text="**Please join my Group before using me.**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="JOIN GROUP", url=f"https://t.me/{FSUB_GROUP}")]
                ])
            )
            joined_channel_2[user_id] = False
            return
        else:
            joined_channel_2[user_id] = True

    # If the user has joined both required channels, send the start message with photo
    start_text = START_TEXT.format(msg.from_user.first_name) if hasattr(msg, "message_id") else START_TEXT
    await bot.send_photo(
        chat_id=user_id,
        photo=SUNRISES_PIC,
        caption=start_text,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Developer ❤️", url="https://t.me/Sunrises_24"),
             InlineKeyboardButton("Updates 📢", url="https://t.me/Sunrises24botupdates")],
            [InlineKeyboardButton("Help 🌟", callback_data="help"),
             InlineKeyboardButton("About 🧑🏻‍💻", callback_data="about")],
            [InlineKeyboardButton("Support ❤️‍🔥", url="https://t.me/Sunrises24botSupport")]
        ]),
        reply_to_message_id=getattr(msg, "message_id", None)
    )

async def check_membership(bot, msg: Message, fsub, joined_channel_dict, prompt_text, join_url):
    user_id = msg.chat.id
    if user_id in joined_channel_dict and not joined_channel_dict[user_id]:
        await msg.reply_text(
            text=prompt_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="Join Now", url=join_url)]
            ])
        )
        return False
    return True

@Client.on_message(filters.private & ~filters.command("start"))
async def handle_private_message(bot, msg: Message):
    user_id = msg.chat.id
    
    # Check membership for updates channel
    if FSUB_UPDATES and not await check_membership(bot, msg, FSUB_UPDATES, joined_channel_1, "Please join my first updates channel before using me.", f"https://t.me/{FSUB_UPDATES}"):
        return
    
    # Check membership for group channel
    if FSUB_GROUP and not await check_membership(bot, msg, FSUB_GROUP, joined_channel_2, "Please join my Group before using me.", f"https://t.me/{FSUB_GROUP}"):
        return
    

                          
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION ABOUT HANDLER
@Client.on_message(filters.command("about"))
async def about_command(bot, msg):
    about_text = """
<b>✯ Mʏ Nᴀᴍᴇ : <a href=https://t.me/MetaMorpher24Bot>𝐌𝐞𝐭𝐚𝐌𝐨𝐫𝐩𝐡𝐞𝐫 🌟</a></b>
<b>✯ Dᴇᴠᴇʟᴏᴘᴇʀ 🧑🏻‍💻 : <a href=https://t.me/Sunrises_24>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™ ⚡</a></b>
<b>✯ Uᴘᴅᴀᴛᴇs 📢 : <a href=https://t.me/Sunrises24BotUpdates>𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢</a></b>
<b>✯ Sᴜᴘᴘᴏʀᴛ ✨ : <a href=https://t.me/Sunrises24BotUpdates>𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ✨</a></b>
<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2.4 [Sᴛᴀʙʟᴇ]</b>
    """
    await msg.reply_text(about_text)

# Function to handle /help command
@Client.on_message(filters.command("help"))
async def help_command(bot, msg):
    help_text = """
    <b>Hᴇʟʟᴏ Mᴀᴡᴀ ❤️
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.

🦋 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Video/File 🖼️

/start - 𝐵𝑜𝑡 𝑎𝑙𝑖𝑣𝑒 𝑜𝑟 𝑁𝑜𝑡 🚶🏻
/mediainfo - mediainfo information of Video & Filesℹ️

🔱 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 : <a href='https://t.me/Sunrises_24'>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™</a></b>
    
   """
    await msg.reply_text(help_text)



#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION CALLBACK HELP
@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "Sᴇɴᴅ ᴀ ғɪʟᴇ ᴀɴᴅ /rename <new name> ᴡɪᴛʜ ʀᴇᴘʟᴀʏᴇᴅ ʏᴏᴜʀ ғɪʟᴇ\n\n"
    txt += "Rᴇɴᴀᴍᴇ [#𝟸GB] Bᴇʟᴏᴡ - Tᴇʟᴇɢʀᴀᴍ [#𝟸GB] Aʙᴏᴠᴇ - Gᴏᴏɢʟᴇ Dʀɪᴠᴇ - Rᴇɴᴀᴍᴇ ғɪʟᴇꜱ\n\n"
    txt += "Mᴇᴛᴀᴅᴀᴛᴀ - Mᴏᴅɪғʏ ᴍᴇᴛᴀᴅᴀᴛᴀ\n\nFᴏʀᴍᴀᴛ: ᴄʜᴀɴɢᴇᴍᴇᴛᴀᴅᴀᴛᴀ ᴠɪᴅᴇᴏ_ᴛɪᴛʟᴇ | ᴀᴜᴅɪᴏ_ᴛɪᴛʟᴇ | ꜱᴜʙᴛɪᴛʟᴇ_ᴛɪᴛʟᴇ\n\n"
    txt += "Gᴏғɪʟᴇ - Tʜᴇ Fɪʟᴇs Uᴘʟᴏᴀᴅ Tᴏ Gᴏғɪʟᴇ Lɪɴᴋ 🔗\n\n"
    txt += "ɢᴏғɪʟᴇsᴇᴛᴜᴘ - Sᴇᴛᴜᴘ Tʜᴇ Gᴏғɪʟᴇ API KEY ғʀᴏᴍ Gᴏғɪʟᴇ.ɪᴏ ⚙️\n\n"
    txt += "ɢᴅʀɪᴠᴇɪᴅ - Tʜᴇ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ Fᴏʟᴅᴇʀ ID Sᴇᴛᴜᴘ 📁.\n\n"
    txt += "Mɪʀʀᴏʀ - Mɪʀʀᴏʀ ғɪʟᴇs ᴛᴏ ᴀ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ʟɪɴᴋ.\n\n"
    txt += "Cʟᴏɴᴇ -  Cʟᴏɴᴇ ᴀ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ʟɪɴᴋ.\n\n"
    txt += "Lɪsᴛ - Cʜᴇᴄᴋ ᴛʜᴇ ғɪʟᴇs ɪɴ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ᴠɪᴀ ᴛʜᴇ ʙᴏᴛ.\n\n"
    txt += "Cʟᴇᴀɴ - Dᴇʟᴇᴛᴇ ғɪʟᴇs ɪɴ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ʙʏ ғɪʟᴇ ɴᴀᴍᴇ.\n\n"
    txt += "ʟᴇᴇᴄʜ - ʟᴇᴇᴄʜ ᴛʜᴇ Sᴇᴇᴅʀ & Wᴏʀᴋᴇʀs' Lɪɴᴋs ᴛᴏ Fɪʟᴇ ᴏʀ Gᴅʀɪᴠᴇ.\n\n"
    txt += "Exᴛʀᴀᴄᴛ Aᴜᴅɪᴏs - Exᴛʀᴀᴄᴛ ᴀᴜᴅɪᴏ ғʀᴏᴍ ғɪʟᴇs.\n\n"
    txt += "Exᴛʀᴀᴄᴛ Sᴜʙᴛɪᴛʟᴇs - Exᴛʀᴀᴄᴛ sᴜʙᴛɪᴛʟᴇs ғʀᴏᴍ ғɪʟᴇs.\n\n"
    txt += "Exᴛʀᴀᴄᴛ Vɪᴅᴇᴏs - Exᴛʀᴀᴄᴛ ᴠɪᴅᴇᴏ ғʀᴏᴍ ғɪʟᴇs.\n\n"
    txt += "Cʜᴀɴɢᴇɪɴᴅᴇxᴀᴜᴅɪᴏ - Rᴇᴀʀʀᴀɴɢᴇ ᴛʜᴇ ɪɴᴅᴇx\n\nFᴏʀᴍᴀᴛ:1)a-𝟷 ғᴏʀ ʀᴇᴍᴏᴠᴇ ᴀᴜᴅɪᴏ\n2)a-𝟸-𝟷-𝟹-𝟺 ғᴏʀ ꜱᴡᴀᴘ ᴀᴜᴅɪᴏ\n\n"
    txt += "Cʜᴀɴɢᴇɪɴᴅᴇxsᴜʙ - Rᴇᴏʀᴅᴇʀ ᴛʜᴇ sᴇǫᴜᴇɴᴄᴇ [s-𝟷  ғᴏʀ ʀᴇᴍᴏᴠᴇ sᴜʙᴛɪᴛʟᴇ, s-𝟸-𝟷-𝟹-𝟺 ғᴏʀ sᴡᴀᴘ sᴜʙᴛɪᴛʟᴇ]\n\n"
    txt += "Gᴇɴᴇʀᴀᴛᴇ Sᴀᴍᴘʟᴇ Vɪᴅᴇᴏ - Cʀᴇᴀᴛᴇ ꜱᴀᴍᴘʟᴇ ᴠɪᴅᴇᴏꜱ (𝟹𝟶ꜱ, 𝟼𝟶ꜱ, 𝟿𝟶ꜱ, 𝟷𝟸𝟶ꜱ, 𝟷𝟻𝟶ꜱ)\n\n"
    txt += "Sᴄʀᴇᴇɴꜱʜᴏᴛꜱ - Tᴀᴋᴇ ꜱᴄʀᴇᴇɴꜱʜᴏᴛꜱ (ᴇxᴀᴍᴘʟᴇ: /ꜱᴄʀᴇᴇɴꜱʜᴏᴛꜱ 𝟷𝟶)\n\n"
    txt += "Uɴᴢɪᴘ ᴛʜᴇ Fɪʟᴇꜱ ᴏɴʟʏ ᴢɪᴘ Fᴏʀᴍᴀᴛ ᴏɴʟʏ - Exᴛʀᴀᴄᴛ ZIP ғɪʟᴇꜱ ᴏɴʟʏ\n\n"
    txt += "Aᴛᴛᴀᴄʜ Pʜᴏᴛᴏ ɪꜱ ᴜꜱᴇᴅ ᴀᴛᴛᴀᴄʜᴍᴇɴᴛ.ɪᴘɢ ᴛᴏ ᴀ ғɪʟᴇ\n\n"
    txt += "ꜱᴇᴛᴘʜᴏᴛᴏ -  Tᴏ ᴀᴅᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴀ ғɪʟᴇ  ᴀᴛᴛᴀᴄʜᴍᴇɴᴛ.ɪᴘɢ ғᴏʀ ꜱᴇɴᴅɪɴɢ ᴛʜᴇ ᴘʜᴏᴛᴏ ᴀꜱ ᴀɴ ᴀᴛᴛᴀᴄʜᴍᴇɴᴛ.\n\n"
    txt += "ᴍᴇʀɢᴇ  - Sᴇɴᴅ ᴜᴘ ᴛᴏ 𝟷𝟶 ᴠɪᴅᴇᴏ/ᴅᴏᴄᴜᴍᴇɴᴛ ғɪʟᴇs ᴏɴᴇ ʙʏ ᴏɴᴇ.\n\n"
    txt += "ᴠɪᴅᴇᴏᴍᴇʀɢᴇ - Vɪᴅᴇᴏᴍᴇʀɢᴇ ᴡɪᴛʜ ғɪʟᴇɴᴀᴍᴇ.ᴍᴋᴠ ᴛᴏ sᴛᴀʀᴛ ᴍᴇʀɢɪɴɢ\n\n"
    txt += "Mᴜʟᴛɪᴛᴀsᴋ - Mᴜʟᴛɪᴛᴀsᴋ ɪs Cʜᴀɴɢᴇᴍᴇᴛᴅᴀᴛᴀ + Tʜᴜᴍʙɴᴀɪʟ\n\n"
    txt += "RᴇᴍᴏᴠᴇTᴀɢs - Tᴏ Rᴇᴍᴏᴠᴇ Aʟʟ Mᴇᴛᴀᴅᴀᴛᴀ Tᴀɢs\n\n"
    txt += "ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄ🌟\n\n"
    txt += "/view ᴛᴏ ꜱᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ 👀\n\n"
    txt += "/del ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ❌\n\n"
    txt += "Jᴏɪɴ : @Sunrises24BotUpdates"
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")   
    ]] 
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#FUNCTION CALL BACK ABOUT
@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Dᴇᴠᴇʟᴏᴘᴇʀ ="<a href=https://t.me/Sunrises_24>SUNRISES™🧑🏻‍💻</a>"     
    txt="<b>Uᴘᴅᴀᴛᴇs 📢: <a href=https://t.me/Sunrises24botupdates>SUNRISES™</a></b>"
    txt="<b>Sᴜᴘᴘᴏʀᴛ ✨: <a href=https://t.me/Sunrises24botSupport>SUNRISES⚡™</a></b>"
    txt="<b>✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs 📊 : ᴠ2.4 [Sᴛᴀʙʟᴇ]</b>" 
    button= [[        
        InlineKeyboardButton("Cʟᴏꜱᴇ ❌", callback_data="del")       
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return

#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
#Ping
@Client.on_message(filters.command("ping"))
async def ping(bot, msg):
    start_t = time.time()
    rm = await msg.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!📍\n{time_taken_s:.3f} ms")
 
