from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Получение токена из переменных среды
TOKEN = "8189759661:AAF2cXuG9O9ntkbXoeabaszFgZnayNu7lCs"


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я бот твой AI ассистент! Чем я могу тебе помочь?")

# Основная точка входа
if __name__ == "__main__":
    if not TOKEN:
        print("Ошибка: Токен не найден. Проверьте переменные среды.")
        exit(1)

    # Создание приложения и добавление обработчика команды /start
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    # Использование polling вместо вебхука
    application.run_polling()

    print("Бот работает с polling!")
