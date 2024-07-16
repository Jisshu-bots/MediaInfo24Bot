#SUNRISES24BOTS
#TG:@SUNRISES_24

import os
from flask import Flask, request
from pyrogram import Client
from config import *

# Initialize Flask app
app = Flask(__name__)

# Initialize Pyrogram Client
app_client = Client(
    "MetaMorpher",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "main"}
)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    app_client.process_update(update)
    return "OK", 200

if __name__ == '__main__':
    if not os.path.isdir(config.DOWNLOAD_LOCATION):
        os.makedirs(config.DOWNLOAD_LOCATION)
    
    app_client.start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    app_client.stop()
