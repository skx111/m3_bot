import sqlite3
from aiogram import types, Dispatcher
from config import bot, ADMIN_ID
from database.sql_commands import Database
from keyboards.inline_button import questionnaire_keyboard, save_button
from scraping.news_scraper import NewsScraper
from scraping.async_news import AsyncNewsScraper
import re



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

# async def save_service_call(call: types.CallbackQuery):
#     link = re.search(r'(https?://\S+)', call.message.text)
#     if link:
#         Database().sql_insert_service_commands(link=link.group(0))
#
#     await bot.send_message(chat_id=call.from_user.id, text='You saved the link')


async def async_service(call: types.CallbackQuery):
    # data = await AsyncScraper().async_scrapers()
    data = await AsyncNewsScraper().async_crapers()
    links = AsyncNewsScraper.PLUS_URL
    for link in data:
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Services O!:"
                               f"\n{links}{link}", reply_markup=await save_button())





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
    dp.register_callback_query_handler(async_service,
                                       lambda call: call.data == "async_service")
    # dp.register_callback_query_handler(save_service_call,
    #                                    lambda call: call.data == "save_service_call")
