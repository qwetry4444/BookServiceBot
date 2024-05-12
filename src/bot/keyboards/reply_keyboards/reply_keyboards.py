from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🔎 Поиск")
    kb.button(text="📚 Моё")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_user_book_type_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="✅ Прочитанные")
    kb.button(text="📚 Отложенные")
    kb.button(text="⬅ Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_search_criteria_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="📄 Название")
    kb.button(text="💫 Жанр")
    kb.button(text="⭐ Рейтинг")
    kb.button(text="⬅ Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
