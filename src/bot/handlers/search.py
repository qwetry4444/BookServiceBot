from aiogram import Router, F
from aiogram.types import Message

from src.bot.keyboards.reply_keyboards import get_search_criteria_kb

router = Router()


@router.message(F.text.lower() == "🔎 поиск")
async def search(message: Message):
    await message.answer(
        "Выберите критерий поиска",
        reply_markup=get_search_criteria_kb()
    )


@router.message(F.text.lower() == "название")
async def search(message: Message):
    await message.answer(
        "Выберите критерий поиска",
        reply_markup=get_search_criteria_kb()
    )


@router.message(F.text.lower() == "жанр")
async def search(message: Message):
    await message.answer(
        "Выберите критерий поиска",
        reply_markup=get_search_criteria_kb()
    )


@router.message(F.text.lower() == "рейтинг")
async def search(message: Message):
    await message.answer(
        "Выберите критерий поиска",
        reply_markup=get_search_criteria_kb()
    )
