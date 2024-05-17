from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(
        f"Hello {user.first_name}! \nI can help you remove audio tracks from videos. Send me a video file to get started."
    )