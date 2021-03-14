import os
import random
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from content import WORDS, INSTRUCTIONS, START_INSTRUCTIONS

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('ARTEM_CHAT_ID')

bot = Bot(token=TG_TOKEN)


def send_start_message(bot, update):
    bot.message.reply_text(START_INSTRUCTIONS)


def send_random_word(bot, update):
    dict_to_list = list(WORDS.items())
    random_words_set = random.choice(dict_to_list)
    bot.message.reply_text(
        '{eng_w} - {rus_w}'.format(
            eng_w=random_words_set[0],
            rus_w=random_words_set[1]
        )
    )


def send_instructions(bot, update):
    bot.message.reply_text(INSTRUCTIONS)


updater = Updater(token=TG_TOKEN)
updater.start_polling(poll_interval=5)
updater.dispatcher.add_handler(CommandHandler('start', send_start_message))
updater.dispatcher.add_handler(CommandHandler(
    'instructions', send_instructions
    )
)
updater.dispatcher.add_handler(CommandHandler('words', send_random_word))
