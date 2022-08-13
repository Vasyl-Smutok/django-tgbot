from django.core.management.base import BaseCommand
from aiogram.utils import executor

from tgbot_manage import bot


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        executor.start_polling(bot.dp)
        return
