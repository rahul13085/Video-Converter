from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):

    update.message.reply_text("Here are some commands you can use:\n/start - Start the bot\n/help - Show this help message\nSend me a video file to remove its audio track.")