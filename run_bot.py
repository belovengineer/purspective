import aiogram
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.inline_keyboards import InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

@dp.message(CommandStart()) # принимаю команду start и вывожу сообщение
async def command_start_handler(message: Message):
    await message.answer("Привет! Введи сумму в RUB, а я переведу его в USD")

@dp.message() # принимаю любое сообщение и перевожу из рублей в доллары
async def get_currency_comverter(message: Message):
    currency_rate_rub_usd = 0.012783
    currency_calc = round(float(message.text.replace(',', '.')) * currency_rate_rub_usd, 2)
    await message.answer(f"{message.text} RUB - {currency_calc} USD")

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())