import os
import threading
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Токен берется из переменных окружения Render
TOKEN = os.environ.get("TELEGRAM_TOKEN") 
WORD = "хуй"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- Код бота ---
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WORD)

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

# --- Веб-сервер для Render ---
web_app = Flask(__name__)

@web_app.route('/')
@web_app.route('/health')
def health():
    return "Bot is running", 200

if __name__ == '__main__':
    # Запускаем бота в фоне
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    # Запускаем Flask, чтобы Render видел открытый порт
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)
