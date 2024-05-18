import os
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = '6803340220:AAHDEwHIDtsu6eflm8a9o6-mKRJ7_1DPbqw'

WEBHOOK_HOST = 'video-converter-11.onrender.com'
WEBHOOK_PORT = 443
WEBHOOK_URL_PATH = '/webhook'
WEBHOOK_URL = f"https://video-converter-11.onrender.com/webhook"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the bot.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a help message.')

async def process_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Processing video...')

async def main():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        logger.info('Asyncio loop is already running. Exiting the script.')
    else:
        application = Application.builder().token(BOT_TOKEN).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help))
        application.add_handler(MessageHandler(filters.VIDEO & ~filters.Document.ALL, process_video))

        await application.initialize()
        await application.bot.set_webhook(url=WEBHOOK_URL)
        await application.run_webhook(
            listen="0.0.0.0",
            port=int(WEBHOOK_PORT),
            url_path=WEBHOOK_URL_PATH,
            webhook_url=WEBHOOK_URL
        )
        await application.shutdown()

if __name__ == '__main__':
    asyncio.run(main())
