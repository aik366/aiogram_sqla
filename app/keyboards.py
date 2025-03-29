from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def menu_user():
    Builder = ReplyKeyboardBuilder()
    Builder.add(KeyboardButton(text="➕ Добавить контакт"))
    Builder.add(KeyboardButton(text="📖 Показать контакты"))
    Builder.add(KeyboardButton(text="🗑 Удалить контакт"))
    Builder.add(KeyboardButton(text="🔎 Поиск контакта"))
    Builder.add(KeyboardButton(text="Чат GPT"))
    Builder.adjust(2)
    return Builder.as_markup(resize_keyboard=True)


def menu_admin():
    Builder = ReplyKeyboardBuilder()
    Builder.add(KeyboardButton(text="➕ Добавить контакт"))
    Builder.add(KeyboardButton(text="📖 Показать контакты"))
    Builder.add(KeyboardButton(text="🗑 Удалить контакт"))
    Builder.add(KeyboardButton(text="🔎 Поиск контакта"))
    Builder.add(KeyboardButton(text="🔧 Настройки"))
    Builder.adjust(2)
    return Builder.as_markup(resize_keyboard=True)


def site_menu():
    Builder = InlineKeyboardBuilder()
    Builder.add(InlineKeyboardButton(text="DeepSeek", url="https://deepseek.com/"))
    Builder.add(InlineKeyboardButton(text="Qwen", url="https://chat.qwenlm.ai/"))
    Builder.add(InlineKeyboardButton(text="Google", url="https://www.google.com/"))
    Builder.add(InlineKeyboardButton(text="Yandex", url="https://yandex.ru/"))
    Builder.adjust(2)
    return Builder.as_markup(resize_keyboard=True)


def yes_no():
    Builder = InlineKeyboardBuilder()
    Builder.add(InlineKeyboardButton(text="✅ Да", callback_data="yes"))
    Builder.add(InlineKeyboardButton(text="✖️ Нет", callback_data="no"))
    return Builder.as_markup(resize_keyboard=True)
