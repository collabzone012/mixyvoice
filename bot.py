#!/usr/bin/env python3
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set your bot token here
TOKEN = os.getenv("BOT_TOKEN") or "7686570410:AAFtY6sAcgKAG15mc8B3GyclKsG7sscebj0"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    update.message.reply_text("🚀 Hello Mixy! Bot is ready.")

def help_command(update, context):
    update.message.reply_text("/start - start the bot\n/help - this help message")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
