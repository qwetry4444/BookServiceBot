from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.bot.keyboards.inline_keyboards import get_books_heads_kb
from ..fsm_groups import SearchStates


router = Router()


@router.message(StateFilter(SearchStates.search_by_title))
async def search_start(message: Message, api_helper):
    books_heads = api_helper.search_bookheads_by_title(message.text)
    await message.answer(
        f"Ищем это --> {message.text}",
        reply_markup=get_books_heads_kb(books_heads)
    )

