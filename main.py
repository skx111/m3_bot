from aiogram import executor
from config import dp
from handlers import (start, )
from database import sql_commands



async def on_start(_):
    db = sql_commands.Database()
    db.sql_create_table()



start.register_start_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_start
    )