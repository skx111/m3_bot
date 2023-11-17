import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_button import start_keyboard
from profanity_check import predict, predict_prob

async def chat_message(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -4062917267:
        ban_word_predict_prob = predict_prob([message.text])
        if ban_word_predict_prob > 0.1:
            await message.delete()
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                     f"Dont curse in this chat!"
            )

            user = db.sql_select_ban_user(
                telegram_id=message.from_user.id
            )
            print(user)
            # if not user:
            #     db.sql_insert_users(
            #         telegram_id=message.from_user.id
            #     )
            # elif user:
            #     db.sql_update_ban_user_count(
            #         telegram_id=message.from_user.id
            #     )




        # db.sql_insert_ban_user(
        #     telegram_id=message.from_user.id
        # )


    else:
        await message.reply(
            text='There is no such a command'
    )




def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_message)