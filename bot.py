import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config

from handlers import start, user_books, search


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(start.router, user_books.router, search.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
