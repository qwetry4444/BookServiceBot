import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from sqlalchemy.engine import URL  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.db.database import create_async_engine, get_session_maker, Database
# from config_reader import config
from src.bot.middlewares.database_middleware import DatabaseMiddleware
from src.bot.middlewares.register_check import RegisterCheck
from src.bot.handlers import set_search_type_handler, user_books_handler, start_handler, search_processing_handler, about_book_handler
from src.open_library_api.api import ApiHelper


async def main():
    load_dotenv()

    dp = Dispatcher()
    dp.include_routers(
        start_handler.router,
        user_books_handler.router,
        search_processing_handler.router,
        set_search_type_handler.router,
        about_book_handler.router
    )

    dp.message.middleware(DatabaseMiddleware())
    dp.message.middleware(RegisterCheck())

    bot = Bot(getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)

    name: str = getenv("POSTGRES_DATABASE")
    user: str = getenv("POSTGRES_USER")
    passwd: str = getenv("POSTGRES_PASSWORD")
    port: int = int(getenv("POSTGRES_PORT"))
    host: str = getenv("POSTGRES_HOST")

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    postgres_url = URL.create(
        drivername=f"{database_system}+{driver}",
        username=user,
        database=name,
        password=passwd,
        port=port,
        host=host,
    ).render_as_string(hide_password=False)
    print(postgres_url)

    async_engine = create_async_engine(postgres_url)
    api_helper = ApiHelper()

    await dp.start_polling(bot, engine=async_engine, api_helper=api_helper)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
