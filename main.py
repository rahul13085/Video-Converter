import os
import logging
from telegram import Update, ForceReply, File
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from config import BOT_TOKEN, API_HASH
from asyncio import Queue
from telegram.ext import Updater, Dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
update_queue = Queue()
updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
updater = Updater(BOT_TOKEN, update_queue=update_queue)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(filters.video & ~filters.document, process_video))

updater.start_polling()
updater.idle()
