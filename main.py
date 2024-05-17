import os
import logging
from telegram import Update, ForceReply, File
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from config import BOT_TOKEN, API_HASH

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(filters.video & ~filters.document, process_video))

updater.start_polling()
updater.idle()
