import os
import random

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    Updater, CommandHandler, CallbackQueryHandler, CallbackContext
)

from dotenv import load_dotenv

from content import MAIN_MENU_MESSAGE, WORDS


# Execution functions.


def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        main_menu_message(),
        reply_markup=main_menu_keyboard())


def main_menu(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        main_menu_message(),
        reply_markup=main_menu_keyboard())


def study_info_main(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        study_info_main_message(),
        reply_markup=study_info_main_keyboard()
    )


def send_random_word(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        send_random_word_message(),
        reply_markup=send_random_word_keyboard()
    )


# Keyboards.

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Узнать про обучение.', callback_data='m1'),
            InlineKeyboardButton('Узнать новое слово!', callback_data='m2'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def study_info_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Вернуться в начало.', callback_data='main'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def send_random_word_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Еще слово!', callback_data='m2'),
            InlineKeyboardButton('Вернуться в начало.', callback_data='main'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# Messages.

def main_menu_message():
    return MAIN_MENU_MESSAGE


def study_info_main_message():
    return 'Здесь инфо про обучение.'


def send_random_word_message():
    """ Chooses random word from the WORDS dictionary. """
    dict_to_list = list(WORDS.items())
    random_words_set = random.choice(dict_to_list)
    message = '{eng_w} - {rus_w}'.format(
            eng_w=random_words_set[0],
            rus_w=random_words_set[1])
    return message


# Handlers.

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')

updater = Updater(token=TG_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(
    study_info_main, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(
    send_random_word, pattern='m2'))
# updater.dispatcher.add_error_handler(error)

updater.start_polling()

updater.idle()
