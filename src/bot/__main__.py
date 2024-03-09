import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from sqlalchemy.engine import URL  # type: ignore

from src.db.database import create_async_engine, get_session_maker
from config_reader import config

from src.bot.handlers import search, user_books, start


async def main():
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        user_books.router,
        search.router)

    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=config.postgres_user,
        host=config.host,
        database=config.database,
        port=config.port,
        password=config.password
    )
    
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)

    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
