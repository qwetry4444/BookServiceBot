from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.open_library_api.api import ApiHelper
from olclient import Book, BookHead, Author


def get_books_heads_kb(book_head_list: [BookHead]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    if book_head_list:
        for book_head in book_head_list:
            if book_head:
                kb.row(
                    InlineKeyboardButton(
                        text=f"{book_head.title} | {book_head.author_name[0]} | {book_head.publish_year}",
                        callback_data=book_head.key))
    # kb.adjust(2)
    return kb.as_markup(resize_keyboard=False)


def get_book_menu_kb(book: Book) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="💬 Подробнее", callback_data=f"{book.key}|Description"),
            InlineKeyboardButton(text="👴 Автор", callback_data=f"{book.key}|Author")
        ],
        [
            InlineKeyboardButton(text="✅ Прочитано", callback_data=f"{book.key}|Readed"),
            InlineKeyboardButton(text="📚 Отложить", callback_data=f"{book.key}|Futher")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_author_menu_kb(author: Author) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="💬 Подробнее", callback_data=f"{author.identifiers}|Description"),
            InlineKeyboardButton(text="📚 Книги автора", callback_data=f"{author.identifiers}|Books")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_subjects_menu_kb() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="💕 Роман", callback_data="1"),
            InlineKeyboardButton(text="😭 Драма", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🌍 Путешествие", callback_data="1"),
            InlineKeyboardButton(text="👽 Фэнтэзи", callback_data="1")
        ],
        [
            InlineKeyboardButton(text="🔎 Детектив", callback_data="1"),
            InlineKeyboardButton(text="📈 Саморазвитие", callback_data="1")
        ]

    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
