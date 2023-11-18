from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'Start Questionnaire📃',
        callback_data='start_questionnaire'
    )
    registration_button = InlineKeyboardButton(
        'Registration😃',
        callback_data='registration'
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    white_button = InlineKeyboardButton(
        'White!',
        callback_data='white'
    )
    black_button = InlineKeyboardButton(
        'Black!',
        callback_data='black'
    )
    markup.add(white_button)
    markup.add(black_button)
    return markup
