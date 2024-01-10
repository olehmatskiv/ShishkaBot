from aiogram import Bot , Dispatcher , types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, ласкаво просимо в Shishka Lounge!!!')

@dp.message()
async def answer(message: types.Message):
    await message.reply('Я вмію спілкуватися як людина, я звичайнісінькій бот)')

if __name__ == '__main__':
    dp.start_polling(bot)