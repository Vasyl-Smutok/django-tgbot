from django.apps import AppConfig
from aiogram.utils import executor

from tgbot_manage import bot


class TgbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tgbot_manage'

    def ready(self):
        executor.start_polling(bot.dp)
