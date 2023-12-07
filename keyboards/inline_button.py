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
    my_profile_button = InlineKeyboardButton(
        'My profile😎',
        callback_data='my_profile'
    )
    random_profiles_button = InlineKeyboardButton(
        'View profiles🔍',
        callback_data='random_profiles'
    )
    reference_menu_button = InlineKeyboardButton(
        'Reference Menu📖',
        callback_data='reference_menu'
    )
    news_button = InlineKeyboardButton(
        "Latest News",
        callback_data="news"
    )
    async_news_button = InlineKeyboardButton(
        "Async Latest News",
        callback_data="async_latest_news"
    )


    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(random_profiles_button)
    markup.add(reference_menu_button)
    markup.add(news_button)
    markup.add(async_news_button)
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


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"liked_profile_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete",
        callback_data="delete_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        'Reference Link🔗',
        callback_data='reference_link'
    )
    reference_list_button = InlineKeyboardButton(
        'Referral List',
        callback_data='reference_list'
    )
    markup.add(reference_button)
    markup.add(reference_list_button)
    return markup

async def save_button():
    markup = InlineKeyboardMarkup()
    save_service = InlineKeyboardButton(
        "save",
        callback_data='save_service'
    )
    markup.add(save_service)
    return markup
