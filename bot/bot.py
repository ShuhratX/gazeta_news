import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from news.check_news import fetch_news

API_TOKEN = '7336413831:AAHMdJXF81dPh954B_HfeQVWH-CAQUfVNJI'

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher ni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Middlewares
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        f"Assalomu alaykum {message.from_user.full_name}. Men gazeta.uz internet nashrining so'ngi xabarlarini tekshiruvchi "
        "telegram botman!\nXabarlani ko'rish uchun /latest buyrug'ini bosing!")


@dp.message_handler(commands="latest")
async def get_news(message: types.Message):  # Oxirgi 10 ta xabarni olish funksiyasi
    news = fetch_news()
    for msg in news:
        await message.answer(
            f"{msg['category']}\n{msg['title']}\n{msg['content']}"
        )


def start_bot():  # Bu botni ishga tushirish funksiyasi
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    executor.start_polling(dp, skip_updates=True, loop=loop)
