import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_button import questionnaire_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class RegistrationStates(StatesGroup):
    nickname = State()
    bio = State()
    geo = State()
    gender = State()
    age = State()
    photo = State()

async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me your nickname'
    )
    await RegistrationStates.nickname.set()

async def load_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Tell me about yourself'
    )
    await RegistrationStates.next()

async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Where are u from?'
    )
    await RegistrationStates.next()

async def load_geo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['geo'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='What is your gender?'
    )
    await RegistrationStates.next()

async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old are you?'
    )
    await RegistrationStates.next()

async def load_age(message: types.Message, state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Use only numeric text!\n'
                 'Register again!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me your photo'
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message, state: FSMContext):
    path = await message.photo[0].download(
        destination_dir=DESTINATION
    )
    print(path.name)
    # async with state.proxy() as data:
    #     await bot.send_message(
    #         chat_id=message.from_user.id,
    #         text='How old are you?'
    #     )




def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == 'registration'
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_geo,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
