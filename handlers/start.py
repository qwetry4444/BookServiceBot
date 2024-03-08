from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.reply_keyboards import get_menu_kb

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.username}!\n",
        reply_markup=get_menu_kb()
    )


@router.message(F.text.lower() == "назад")
async def back(message: Message):
    await message.answer(
        "Меню",
        reply_markup=get_menu_kb()
    )
