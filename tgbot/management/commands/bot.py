from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import CallbackContext, Filters, Updater, MessageHandler, CommandHandler
from telegram.utils.request import Request

from website.models import Service, Recording


def log_errors(data):
    def wrapper(*args, **kwargs):
        try:
            return data(*args, **kwargs)
        except Exception as error:
            error_message = f'Произошла ошибка: {error}'
            print(error_message)
            raise error
    return wrapper


@log_errors
def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    reply_text = f'Извините наш бот не поддерживает команду: "{text}"'
    update.message.reply_text(text=reply_text)


@log_errors
def do_count_records(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Recording.objects.get_or_create(external_id=chat_id, defaults={})

class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(request=request, token=settings.TELEGRAM_TOKEN)
        print(bot.get_me())

        updater = Updater(bot=bot, use_context=True)

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        message_handler2 = CommandHandler('count', do_count_records)
        updater.dispatcher.add_handler(message_handler2)

        updater.start_polling()
        updater.idle()

