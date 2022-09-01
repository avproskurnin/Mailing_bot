from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from logger_bot import logger

from telegram.ext import CallbackContext
from shp_mailing_bot.prep import Prep


def get_support_informatics(update: Update, context: CallbackContext):
    logger.info(f"[{update.effective_user.name}] got support informatics link")
    update.message.reply_text(f"@supeduapp — сюда вы можете обратиться, если у вас возникла проблема с Информатикс. "
                              f"\nПоддержка работает 5/2 с 9:30 до 18:00 ☘️")

