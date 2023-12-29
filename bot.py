# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyromod import listen


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


DOWNLOAD_LOCATION = "/downloads"

if __name__ == "__main__" :
    
    plugins  = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        ":memory:",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,        
        plugins=plugins,
        parse_mode="html"
    )
    Config.AUTH_USERS.add(5793708681)
    print("Bot Started!")
    app.run()
