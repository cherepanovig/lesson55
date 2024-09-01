#Домашнее задание по теме "Методы отправки сообщений".

# Установлен Aiogram последней версии для Python 3.12!!!

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = 'My_TOKEN'

# Инициализируем bot и dispatcher с FSM storage
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Команда start
@dp.message(Command("start"))
async def start_form(message: Message):
    #print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@dp.message()
async def all_messages(message: Message):
    #print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())