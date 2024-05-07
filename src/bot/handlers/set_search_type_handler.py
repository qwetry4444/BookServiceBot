from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from src.bot.keyboards.reply_keyboards.reply_keyboards import get_search_criteria_kb
from src.bot.keyboards.inline_keyboards.inline_keyboards import get_subjects_menu_kb
from ..fsm_groups import SearchStates

router = Router()


@router.message(F.text.lower() == "🔎 поиск")
async def search_start(message: Message):
    await message.answer(
        "Выберите критерий поиска",
        reply_markup=get_search_criteria_kb()
    )


@router.message(F.text.lower() == "📄 название")
async def search_by_title(message: Message, state: FSMContext):
    await message.answer(
        "Введите название книги:",
    )
    await state.set_state(SearchStates.search_by_title)


@router.message(F.text.lower() == "💫 жанр")
async def search(message: Message):
    await message.answer(
        "Выберите жанр",
        reply_markup=get_subjects_menu_kb()
    )


@router.message(F.text.lower() == "⭐ рейтинг")
async def search(message: Message):
    await message.answer(
        "Книги отсортированные по рэйтингу",
        reply_markup=get_search_criteria_kb()
    )
