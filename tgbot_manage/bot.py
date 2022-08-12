import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from tgbot_manage.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Вітаю, я тестовий бот, який був створений, щоб мого розробника взяли на роботу)\n"
        "\nПоки що мій все що я вмію це - реєстрування користувачів, але я впевнений Хазяїн з часом розширить мій функціонал)"
    )


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Моє завдання реєструвати користувачів, щоб зараєструватись набери на клавіатурі  '/registration'")


@dp.message_handler(commands=['registration'])
async def process_registration_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,
        "Розмочинаємо реєстрацію!\n"
    )
    time.sleep(1)
    await bot.send_message(
        msg.from_user.id,
        f"Твої дані:\n \nid-користувача: {msg.from_user.id}"
        f"\nнікнейм: {msg.from_user.username}"
        f"\nім'я: {msg.from_user.first_name}"
        f"\nпрізвище: {msg.from_user.last_name}"
    )

if __name__ == '__main__':
    executor.start_polling(dp)
