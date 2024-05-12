from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.bot.keyboards.inline_keyboards.inline_keyboards import get_books_heads_kb, get_book_menu_kb
from ..fsm_groups import SearchStates
from ...open_library_api.api import ApiHelper

router = Router()


@router.message(StateFilter(SearchStates.search_by_title))
async def search_start(message: Message, api_helper: ApiHelper, state: FSMContext):
    books_heads = api_helper.search_bookheads_by_title(message.text)
    await message.answer(
        "Выберите наиболее подходящее",
        reply_markup=get_books_heads_kb(books_heads)
    )
    await state.set_state(SearchStates.search_by_key)


@router.callback_query(StateFilter(SearchStates.search_by_key))
async def search_by_key(callback: CallbackQuery, api_helper: ApiHelper, state: FSMContext):
    book = api_helper.search_book_by_key(callback.data)
    book_str = api_helper.book_to_str(book)
    await callback.message.answer_photo(photo=api_helper.get_cover_url(book), caption=book_str,
                                        reply_markup=get_book_menu_kb(book))
    await state.clear()
