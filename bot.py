import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

API_TOKEN = '7389036670:AAHrmcoL3NjdZkno92vJyKhUm2Qvd-BN1mo'
CHAT_ID = '645755081'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['id', 'chat_id']))
async def send_chat_id(message: Message):
    await message.reply(f"Your chat ID is {message.chat.id}")


async def send_location(pet_name, phone, latitude, longitude, name):
    location_message = f'Питомец: {pet_name}\nТелефон: {phone}\nКоординаты: {latitude}, {longitude}\nИмя нашедшего: {name}'
    await bot.send_message(CHAT_ID, location_message)
    await bot.send_location(CHAT_ID, latitude, longitude)


if __name__ == '__main__':
    #dp.include_router(dp)
    asyncio.run(dp.start_polling(bot))