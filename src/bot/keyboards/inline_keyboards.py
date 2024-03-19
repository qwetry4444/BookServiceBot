from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.open_library_api.api import ApiHelper
from olclient import Book, BookHead


def get_books_heads_kb(book_head_list: [BookHead]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for book_head in book_head_list:
        kb.row(InlineKeyboardButton(text=f"{book_head.title} | {book_head.author_name[0]} | {book_head.publish_year}", callback_data=book_head.key))
    # kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
