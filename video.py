import os
import logging

from telegram import Update, ForceReply, File
from telegram.ext import CallbackContext

from utils.helpers import send_typing_action

def process_video(update: Update, context: CallbackContext):

    send_typing_action(update, context)

    chat_id = update.effective_chat.id

    if update.message.video:
        video_file = update.message.video

        file_id = video_file.file_id
        file_info = context.bot.get_file(file_id)
        downloaded_file = file_info.download(f"{chat_id}-{file_info.file_name}")

        try:
            os.system(f"ffmpeg -i {downloaded_file} -vn -c copy {
