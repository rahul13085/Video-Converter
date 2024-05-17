from telegram import ChatAction

def send_typing_action(update: Update, context: CallbackContext):
    context.bot.send_chat_action(
        chat_id=update.effective_message.chat_id, action=ChatAction.TYPING
    )