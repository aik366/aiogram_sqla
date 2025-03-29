from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.database.requests import set_user
import app.keyboards as kb

# from middlewares import BaseMiddleware

user = Router()


# user.message.middleware(BaseMiddleware())

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id, message.from_user.full_name)
    await message.answer('Добро пожаловать в бот!', reply_markup=kb.menu_user())


@user.message(F.text == 'Чат GPT')
async def chat_gpt(message: Message):
    await message.answer('Чат GPT', reply_markup=kb.site_menu())
