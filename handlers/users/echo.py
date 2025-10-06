from aiogram import types

from handlers.users.Student import start
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await start(msg=message)
