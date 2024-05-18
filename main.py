import os
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Welcome to the bot.')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('This is a help message.')

def process_video(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Processing video...')

updater = Updater(BOT_TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.video & ~Filters.document, process_video))

updater.start_polling()

updater.idle()
