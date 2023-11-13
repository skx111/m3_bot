import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_button import start_keyboard

async def start_button(message: types.Message):
    print(message)
    db = Database()
    try:
        db.sql_insert_users(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text='Hello',
    #     reply_markup=await start_keyboard()
    # )


    # with open(r'C:\Users\User\PycharmProjects\m3_bot\media\bot-pic.jpeg', 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption='Hello👋',
    #         reply_markup=await start_keyboard()
    #     )


    with open(r'C:\Users\User\PycharmProjects\m3_bot\media\bot-gif.gif' , 'rb') as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption='Hello👋',
            reply_markup=await start_keyboard()
        )





def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])