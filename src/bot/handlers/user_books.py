from aiogram import Router, F
from aiogram.types import Message

from src.bot.keyboards.reply_keyboards import get_user_book_type_kb

router = Router()


@router.message(F.text.lower() == "📚 моё")
async def answer_my(message: Message):
    await message.answer(
        "Посмотреть прочитанные или отолженные книги?",
        reply_markup=get_user_book_type_kb()
    )


@router.message(F.text.lower() == "прочитанные")
async def answer_yes(message: Message):
    await message.answer(
        "Прочитанные вами книги:",

    )


@router.message(F.text.lower() == "отложенные")
async def answer_yes(message: Message):
    await message.answer(
        "Отложенные книги:",

    )
