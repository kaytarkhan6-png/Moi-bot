import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Замените 'ВАШ_ТОКЕН_ЗДЕСЬ' на токен от BotFather
TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"
WORD = "хуй" # То самое слово

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отвечаем на сообщение
    await update.message.reply_text(WORD)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == '__main__':
    main()
