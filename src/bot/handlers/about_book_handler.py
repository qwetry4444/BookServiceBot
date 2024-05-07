from aiogram import Router
from aiogram.types import CallbackQuery

from src.bot.keyboards.inline_keyboards.inline_keyboards import get_author_menu_kb
from ...open_library_api.api import ApiHelper

router = Router()


@router.callback_query()
async def about_book(callback: CallbackQuery, api_helper: ApiHelper):
    book_key = callback.data.split("|")[0]
    action = callback.data.split("|")[1]
    book = api_helper.search_book_by_key(book_key)
    book_str = api_helper.book_to_str(book)

    if action == "Description":
        await callback.message.answer(text=f"Описание: {book.description}")
    elif action == "Author":
        author = api_helper.get_author_of_book(book)
        author_str = api_helper.author_to_str(author)
        await callback.message.answer_photo(photo=api_helper.get_author_photo_url(author), caption=author_str,
                                            reply_markup=get_author_menu_kb(author))
    elif action == "Readed":
        await callback.message.answer(text="Книга добавлена в прочитанные")
    elif action == "Futher":
        await callback.message.answer(text=f"Книга добавлена в отложенные")
