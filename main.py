import time
import os
from telegram import Bot
from loguru import logger
from decouple import config

# BOT_TOKEN = config('BOT_TOKEN', cast=str)
# CHAT_ID = config('CHAT_ID', cast=str)
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
def main():
    bot = Bot(token=BOT_TOKEN)

    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text='ping from heroku')

        except:
            logger.exception('Ошибка всего')

        time.sleep(20 * 60)


if __name__ == '__main__':
    main()