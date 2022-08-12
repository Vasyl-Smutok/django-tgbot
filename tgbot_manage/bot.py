import secrets

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from tgbot_manage.config import TOKEN
from tgbot_manage.airtable import create_records, usernames_in_airtable

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
    await message.reply(
        "Моє завдання реєструвати користувачів, щоб зараєструватись набери на клавіатурі  '/registration'")


@dp.message_handler(commands=['registration'])
async def process_registration_command(msg: types.Message):
    if msg.from_user.username not in usernames_in_airtable():
        password = secrets.token_urlsafe(8)

        await bot.send_message(
            msg.from_user.id,
            "Розмочинаємо реєстрацію!\n \nБільшість інформації береться з "
            "твого акаунта в телегрм, тобі залишиться тільки ввести пароль"
        )

        data = {
            "username": f"{msg.from_user.username}",
            "id": f"{msg.from_user.id}",
            "first_name": f"{msg.from_user.first_name}",
            "last_name": f"{msg.from_user.last_name}",
            "password": f"{password}"
        }

        create_records(data=data)

        await bot.send_message(
            msg.from_user.id,
            f"Твої дані:\n \nid-користувача: {msg.from_user.id}"
            f"\nнікнейм: {msg.from_user.username}"
            f"\nім'я: {msg.from_user.first_name}"
            f"\nпрізвище: {msg.from_user.last_name}"
            f"\nпароль: {password}"
        )

    else:
        await bot.send_message(msg.from_user.id, "Твій нікнейм вже міститься в базі даних\n")
