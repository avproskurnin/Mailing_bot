import sys

from telegram.error import InvalidToken, NetworkError
from telegram.ext import Updater
import shp_mailing_bot.config as config

from shp_mailing_bot.bot import init_dispatcher
from logger_bot import logger


def main():
    try:
        logger.info('Starting...')
        updater = Updater(token=config.TELEGRAM_BOT_TOKEN)
        logger.info('Connection to telegram API established.')

        init_dispatcher(updater)

        logger.info('The bot is alive.')

        # updater.start_polling()

        updater.start_webhook(listen='0.0.0.0',
                              port=5000,
                              url_path='',
                              webhook_url='https://mshpteacherbot.informatics.ru/secretbotfff')
        updater.idle()
    except InvalidToken:
        logger.critical(
            'An incorrect token is specified in the bot settings. Further work of the bot is impossible, stop.')
        sys.exit(101)
    except NetworkError:
        logger.critical('There is no internet connection. Further work of the bot is impossible, stop.')
        sys.exit(102)


if __name__ == "__main__":
    main()
