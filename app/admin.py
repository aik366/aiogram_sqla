from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Filter, CommandStart, Command
from app.keyboards import menu_admin, yes_no
from app.database.requests import select_user, delete_user
from aiogram.fsm.context import FSMContext
from app.states import AdminExample
from config import ADMIN_ID

admin = Router()


class Admin(Filter):
    def __init__(self):
        self.admins = ADMIN_ID

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins


async def result_txt():
    txt = ""
    for key, values in (await select_user()).items():
        txt += f"{key}: {values[0]} {values[1]}\n"
    return txt


@admin.message(Admin(), Command('admin'))
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот, администратор!', reply_markup=menu_admin())


@admin.message(Admin(), F.text == '📖 Показать контакты')
async def cmd_show_contacts(message: Message):
    await message.answer(f'Список контактов\n{await result_txt()}')


@admin.message(Admin(), F.text == '🗑 Удалить контакт')
async def cmd_delete_contact(message: Message, state: FSMContext):
    await message.answer(
        f"Выберите порядковий номер\nпользователя для удаления:\n\n{await result_txt()}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.update_data(user_list=await select_user())
    await state.set_state(AdminExample.delete_id)


@admin.message(AdminExample.delete_id, F.text.isdigit())
async def process_user_id(message: Message, state: FSMContext):
    if len(await state.get_data()) >= int(message.text) > 0:
        user_id = (await state.get_data()).get('user_list')[message.text][0]
        await state.update_data(user_id=user_id)
        await message.answer(f"Подтвердите удаление пользователя с ID {user_id}:", reply_markup=yes_no())
        await state.set_state(AdminExample.confirm_deletion)
    else:
        await message.answer(f"Неверный порядковый номер пользователя.", reply_markup=menu_admin())
        await state.clear()
        await message.answer('Для удаления контакта выберите нужный пункт в меню:', reply_markup=menu_admin())


@admin.callback_query(AdminExample.confirm_deletion, F.data == 'yes')
async def confirm_delete_user(call: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data.get('user_id')
    await delete_user(user_id)
    await call.message.answer(f"Пользователь с ID {user_id} успешно удален.", reply_markup=menu_admin())
    await state.clear()
    await call.answer()


@admin.callback_query(AdminExample.confirm_deletion, F.data == 'no')
async def cancel_delete_user(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Удаление отменено.", reply_markup=menu_admin())
    await state.clear()
    await call.answer()
