import os
import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
TOKEN = os.getenv('6803340220:AAHDEwHIDtsu6eflm8a9o6-mKRJ7_1DPbqw')
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Welcome to the bot.')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('This is a help message.')

def process_video(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Processing video...')
BOT_TOKEN = "6803340220:AAHDEwHIDtsu6eflm8a9o6-mKRJ7_1DPbqw"
application = Application.builder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(MessageHandler(filters.VIDEO & ~filters.Document.ALL, process_video))

application.run_polling()
