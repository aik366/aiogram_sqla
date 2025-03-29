from aiogram.fsm.state import State, StatesGroup


class RegExample(StatesGroup):
    name = State()
    number = State()
    location = State()


class AdminExample(StatesGroup):
    delete_id = State()
    confirm_deletion = State()
