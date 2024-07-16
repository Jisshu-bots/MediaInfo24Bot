import os
import subprocess
from flask import Flask, request
import datetime
from pyrogram import Client, filters
from config import DOWNLOAD_LOCATION
from html_telegraph_poster import TelegraphPoster

# Initialize Flask app
app = Flask(__name__)

# Initialize Telegraph
telegraph = TelegraphPoster(use_api=True)
telegraph.create_api_token("MediaInfoBot")


@app_client.on_message(filters.command("mediainfo") & filters.private)
async def mediainfo_handler(client, message):
    if not message.reply_to_message or (not message.reply_to_message.document and not message.reply_to_message.video):
        await message.reply_text("Please reply to a document or video to get media info.")
        return

    reply = message.reply_to_message
    media = reply.document or reply.video

    # Send an acknowledgment message immediately
    processing_message = await message.reply_text("Getting MediaInfo...")

    try:
        # Download the media file to a local location
        if media:
            file_path = await client.download_media(media, file_name=os.path.join(DOWNLOAD_LOCATION, media.file_name))
        else:
            raise ValueError("No valid media found in the replied message.")

        # Get media info
        media_info_html = get_mediainfo(file_path)

        # Get the current date
        current_date = datetime.datetime.now().strftime("%B %d, %Y")

        # Prepare the media info with additional details using allowed tags
        media_info_html = (
            f"<strong>SUNRISES 24 BOT UPDATES</strong><br>"
            f"<strong>MediaInfo X</strong><br>"
            f"<p>{current_date} by <a href='https://t.me/Sunrises24BotUpdates'>SUNRISES 24 BOT UPDATES</a></p>"
            f"{media_info_html}"
            f"<p>Rights Designed By Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ</p>"
        )

        # Save the media info to a file
        info_file_path = os.path.join(DOWNLOAD_LOCATION, f"{os.path.splitext(media.file_name)[0]}_info.html")
        with open(info_file_path, "w") as info_file:
            info_file.write(media_info_html)

        # Upload the media info to Telegraph
        response = telegraph.post(
            title="MediaInfo",
            author="SUNRISES 24 BOT UPDATES",
            author_url="https://t.me/Sunrises24BotUpdates",
            text=media_info_html
        )
        link = f"https://graph.org/{response['path']}"

        # Prepare the final message with the text file link and the Telegraph link
        message_text = (
            f"SUNRISES 24 BOT UPDATES\n"
            f"MediaInfo X\n"
            f"{current_date} by [SUNRISES 24 BOT UPDATES](https://t.me/Sunrises24BotUpdates)\n\n"
            f"[View Info on Telegraph]({link})\n"
            f"Rights designed by Sᴜɴʀɪsᴇs Hᴀʀsʜᴀ 𝟸𝟺 🇮🇳 ᵀᴱᴸ"
        )

        await message.reply_document(info_file_path, caption=message_text)
    except Exception as e:
        await message.reply_text(f"Error: {e}")
    finally:
        # Clean up the acknowledgment message
        await processing_message.delete()

        # Clean up downloaded files
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        if 'info_file_path' in locals() and os.path.exists(info_file_path):
            os.remove(info_file_path)

if __name__ == '__main__':
    app.run(port=5000)
