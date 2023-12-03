import sqlite3
from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_button import questionnaire_keyboard
from scraping.news_scraper import NewsScraper


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='White or Black?',
        reply_markup=await questionnaire_keyboard()
    )

async def white_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Do u prefer white colour?',
    )

async def black_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Do u prefer black colour?',
    )

async def admin_call(message: types.Message):
    print(ADMIN_ID)
    print(message.from_user.id)
    if message.from_user.id == int(ADMIN_ID):
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Hello master',
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='You are not my master',
        )


async def scraper_call(call: types.CallbackQuery):
    scraper = NewsScraper()
    data = scraper.parse_data()
    for url in data[:5]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"{scraper.PLUS_URL + url}"
        )




def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == 'start_questionnaire')
    dp.register_callback_query_handler(white_call,
                                       lambda call: call.data == 'white')
    dp.register_callback_query_handler(black_call,
                                       lambda call: call.data == 'black')
    dp.register_message_handler(admin_call, lambda word: 'dorei' in word.text)

    dp.register_callback_query_handler(scraper_call,
                                       lambda call: call.data == "news")
